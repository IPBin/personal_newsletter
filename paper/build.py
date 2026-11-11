"""Render an issue (issue.json written by the morning editor) into print-ready PDFs.

    python -m paper.build issues/2026-11-10/issue.json

Outputs next to issue.json:
    paper.pdf          half-letter pages, in reading order (screen / proofing)
    print-booklet.pdf  Letter landscape, 2-up, booklet order -> print double-sided,
                       flip on SHORT edge, fold in half
    preview/page-XX.png
Also updates state/memory.json.
"""
from __future__ import annotations

import copy
import json
import subprocess
import sys
from datetime import date, datetime
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

from . import glyphs, maps
from .impose import impose

ROOT = Path(__file__).resolve().parent.parent
TPL = ROOT / "paper" / "templates"
CSS = ROOT / "paper" / "style.css"


def load_cfg():
    return yaml.safe_load(open(ROOT / "config.yaml"))


def _weather_strip(w):
    out = []
    for i, d in enumerate((w or {}).get("daily", [])[:5]):
        label = "Today" if i == 0 else d["day_of_week"][:3]
        out.append({
            "label": label,
            "icon": glyphs.weather_icon(glyphs.day_kind(d), 26),
            "hi": round(d["high"]), "lo": round(d["low"]),
            "pc": d.get("precipitation_chance", 0) or 0, "ptype": d.get("precipitation_type", ""),
        })
    return out


def _resolve(path_str):
    p = Path(path_str)
    return str(p if p.is_absolute() else (ROOT / p))


def _print_image(path_str, width_in, photo=True):
    """A smaller copy of an image, sized for print, so the PDF stays small enough to email.

    300 pixels per inch is all a laser printer can use for grey art. Photo-like art
    (the back page, plates) is saved as high-quality grayscale JPEG; line art (the
    front band) stays PNG with 16 grey levels. Copies are cached in assets/art/print/.
    """
    from PIL import Image
    src = Path(_resolve(path_str))
    out_dir = ROOT / "assets" / "art" / "print"
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / (src.stem + (".jpg" if photo else ".png"))
    if out.exists() and out.stat().st_mtime >= src.stat().st_mtime:
        return str(out)
    im = Image.open(src).convert("L")
    max_w = int(width_in * 300)
    if im.width > max_w:
        im = im.resize((max_w, round(im.height * max_w / im.width)), Image.LANCZOS)
    if photo:
        im.save(out, "JPEG", quality=82, optimize=True)
    else:
        im.quantize(16).save(out, "PNG", optimize=True)
    return str(out)


def _prepare(issue, cfg):
    """Fill derived visuals (maps, rulers, charts, image paths) into a copy of the issue."""
    iss = copy.deepcopy(issue)
    today = date.fromisoformat(iss["date"])
    if iss.get("front", {}).get("image"):
        iss["front"]["image"]["src"] = _print_image(iss["front"]["image"]["src"], 4.7)
    if iss.get("back"):
        iss["back"]["src"] = _print_image(iss["back"]["src"], 4.6)
    for s in iss["sections"]:
        for b in s["blocks"]:
            if b["type"] == "figure":
                b["src"] = _print_image(b["src"], 4.7)
            if b["type"] == "essay" and b.get("figure"):
                b["figure"]["src"] = _resolve(b["figure"]["src"])
            if b["type"] == "region" and b.get("region"):
                b["map"] = maps.region_map(b["region"], points=b.get("map_points"), width=b.get("map_width", 150))
            if b["type"] == "region" and b.get("chart"):
                b["chart_svg"] = _chart_svg(b["chart"])
            if b["type"] == "chart":
                b["svg"] = _chart_svg(b)
            if b["type"] == "opportunities":
                pts = []
                for g in b["groups"]:
                    for o in g["items"]:
                        if o.get("deadline") and o.get("on_ruler", True):
                            pts.append({"label": o.get("short") or o["name"][:22], "date": date.fromisoformat(o["deadline"])})
                if pts:
                    b["ruler"] = glyphs.deadline_ruler(pts, today, days=b.get("ruler_days", 28), width=306)
    return iss


def _chart_svg(spec):
    kind = spec.get("kind", "bars")
    if kind == "bars":
        return glyphs.bar_chart(spec["rows"], width=spec.get("width", 318), unit=spec.get("unit", ""),
                                max_value=spec.get("max"), label_w=spec.get("label_w", 92))
    if kind == "split":
        return "".join(glyphs.split_bar(r["parts"], total=r.get("total"), width=spec.get("width", 318), label=r.get("label"))
                       for r in spec["rows"])
    raise ValueError(kind)


def _render(iss, cfg, gallery_pages=0, inside=None, pages_label=""):
    env = Environment(loader=FileSystemLoader(TPL), autoescape=True)
    html = env.get_template("issue.html.j2").render(
        issue=iss, cfg=cfg, sections=iss["sections"], css=str(CSS),
        weather=_weather_strip(iss.get("weather")), gallery_pages=gallery_pages,
        gallery=iss.get("gallery") and {**iss["gallery"], "src": _resolve(iss["gallery"]["src"])},
        inside=inside or [], pages_label=pages_label,
    )
    doc = HTML(string=html, base_url=str(ROOT / "paper")).render()
    return html, doc


def _section_pages(doc):
    where = {}
    for i, page in enumerate(doc.pages, start=1):
        for anchor in page.anchors:
            where.setdefault(anchor, i)
    return where


def fit(issue, cfg):
    """Make the issue land on exactly max_pages (a multiple of 4), back page included.

    Too long: drop optional essays, lowest priority first (they become newsstand summaries).
    Too short: add gallery pages (a full-page plate) before the back page, and report it so
    the editor can add more reading next time.
    """
    budget = cfg["layout"]["max_pages"]
    iss = _prepare(issue, cfg)
    demoted = []

    stand_items = [it for s in iss["sections"] for b in s["blocks"] if b["type"] == "newsstand" for it in b["items"]]
    originals = {id(it): copy.deepcopy(it) for it in stand_items}

    def sync():
        """Newsstand follows the essays: a dropped essay shows its fallback summary there.
        Done before every count, because that summary takes space too."""
        present = {b.get("essay_id") for s in iss["sections"] for b in s["blocks"] if b["type"] == "essay"}
        for it in stand_items:
            orig = originals[id(it)]
            if orig.get("mode") == "in full" and it.get("essay_id") not in present:
                it["mode"] = "summary"
                if orig.get("fallback"):
                    it["paras"] = orig["fallback"]
            else:
                it.clear()
                it.update(copy.deepcopy(orig))

    def count():
        # render the way build() does (front-page index and page label included), so the count is the real one
        sync()
        inside = [{"title": s["title"], "page": 9} for s in iss["sections"] if s.get("in_index", True)]
        return len(_render(iss, cfg, inside=inside, pages_label=f"{budget} pages · {budget // 4} sheets · $0.00")[1].pages)

    def locate(block):
        for s in iss["sections"]:
            if block in s["blocks"]:
                return s
        return None

    n = count()
    # 1) drop optional blocks, lowest priority first, until we fit
    while n > budget:
        cand = [(b.get("priority", 0), s, b) for s in iss["sections"] for b in s["blocks"] if b.get("optional")]
        if not cand:
            break
        _, s, b = min(cand, key=lambda t: t[0])
        demoted.append((s, s["blocks"].index(b), b))
        s["blocks"].remove(b)
        n = count()
    # 2) try to put dropped blocks back, highest priority first, if they still fit
    for s, idx, b in sorted(demoted, key=lambda t: -t[2].get("priority", 0)):
        s["blocks"].insert(min(idx, len(s["blocks"])), b)
        m = count()
        if m <= budget:
            n = m
            demoted = [d for d in demoted if d[2] is not b]
        else:
            s["blocks"].remove(b)
    demoted = [d[2] for d in demoted]
    sync()
    target = budget if n > budget - 4 else n + (4 - n % 4) % 4
    gallery = max(0, target - n) if iss.get("gallery") else 0
    return iss, gallery, target, demoted


def build(issue_path: Path):
    cfg = load_cfg()
    issue = json.load(open(issue_path))
    out_dir = issue_path.parent
    iss, gallery, total, demoted = fit(issue, cfg)
    sheets = total // 4
    label = f"{total} pages · {sheets} sheets · ${sheets * 2 * cfg['layout']['cost_per_side']:.2f}"

    # pass 1: find where sections land, pass 2: print the index
    _, doc = _render(iss, cfg, gallery, pages_label=label)
    where = _section_pages(doc)
    inside = [{"title": s["title"], "page": where.get(s["id"], "")} for s in iss["sections"] if s.get("in_index", True)]
    html, doc = _render(iss, cfg, gallery, inside=inside, pages_label=label)
    if len(doc.pages) % 4:
        print(f"WARNING: {len(doc.pages)} pages is not a multiple of 4; the booklet will not impose.")

    (out_dir / "issue.fitted.json").write_text(json.dumps({k: v for k, v in iss.items()}, ensure_ascii=False, indent=1, default=str))
    pdf = out_dir / "paper.pdf"
    doc.write_pdf(pdf)
    (out_dir / "paper.html").write_text(html)
    booklet = impose(pdf, out_dir / "print-booklet.pdf") if len(doc.pages) % 4 == 0 else None

    prev = out_dir / "preview"
    prev.mkdir(exist_ok=True)
    for old in prev.glob("*.png"):
        old.unlink()
    subprocess.run(["pdftoppm", "-r", "110", "-png", str(pdf), str(prev / "page")], check=True)

    if not out_dir.name.startswith("proof"):   # proofs must not rewrite the reading memory
        _update_memory(issue, demoted)
    report = {"pages": len(doc.pages), "sheets": len(doc.pages) // 4, "gallery_pages": gallery,
              "demoted_essays": [d.get("title") for d in demoted],
              "pdf": str(pdf), "booklet": str(booklet) if booklet else None}
    print(json.dumps(report, indent=2))
    return report


def _update_memory(issue, demoted):
    path = ROOT / "state" / "memory.json"
    mem = json.load(open(path)) if path.exists() else {"essays": {}, "opportunities": {}, "issues": []}
    demoted_ids = {d.get("essay_id") for d in demoted}
    for s in issue["sections"]:
        for b in s["blocks"]:
            if b["type"] == "newsstand":
                for it in b["items"]:
                    eid = it.get("essay_id")
                    if not eid:
                        continue
                    mode = "summary" if eid in demoted_ids else it["mode"]
                    rec = mem["essays"].setdefault(eid, {"title": it["title"], "pub": it["pub"], "history": []})
                    rec["history"] = [h for h in rec["history"] if h["date"] != issue["date"]]
                    rec["history"].append({"date": issue["date"], "mode": mode})
                    rec["given_in_full"] = rec.get("given_in_full") or mode == "in full"
            if b["type"] == "opportunities":
                for g in b["groups"]:
                    for o in g["items"]:
                        key = o.get("id") or o["name"]
                        rec = mem["opportunities"].setdefault(key, {"first_seen": issue["date"]})
                        rec.update({"name": o["name"], "deadline": o.get("deadline"), "url": o.get("url"),
                                    "last_seen": issue["date"]})
    if issue["date"] not in mem["issues"]:
        mem["issues"].append(issue["date"])
    path.parent.mkdir(exist_ok=True)
    json.dump(mem, open(path, "w"), indent=2, ensure_ascii=False)


if __name__ == "__main__":
    build(Path(sys.argv[1]).resolve())
