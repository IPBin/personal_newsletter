"""Write the morning email that goes with each issue: what needs you, house rules,
and every citation (the printed paper stays clean; links live here).

    python -m paper.email issues/2026-11-10/issue.json
"""
from __future__ import annotations

import html
import json
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent

HOUSE_RULES = [
    "Plain words, short sentences. No “breaking”, no shouting.",
    "Every story says why it matters. If people disagree, you see both sides.",
    "Opinion is labelled. Essays come whole, with a plain-words summary and the other side.",
    "Newsletters: only the last 24 hours, never the same summary twice.",
    "The paper has an end. That’s the point.",
]


def _url(u: str) -> str:
    u = u.strip()
    if not u or " " in u.split("(")[0].strip() and "." not in u:
        return ""
    return u if u.startswith("http") else "https://" + u.split(" ")[0]


def build(issue_path: Path):
    cfg = yaml.safe_load(open(ROOT / "config.yaml"))
    fitted = issue_path.parent / "issue.fitted.json"
    iss = json.load(open(fitted if fitted.exists() else issue_path))
    rows_news, rows_opps, rows_reads, rows_stand = [], [], [], []
    attention = []
    for s in iss["sections"]:
        for b in s["blocks"]:
            if b["type"] == "attention":
                attention = b["items"]
            if b["type"] == "region":
                for st in b["stories"]:
                    rows_news.append((b["title"], st["headline"], st["outlet"], st["date"], st.get("url", "")))
            if b["type"] == "opportunities":
                for g in b["groups"]:
                    for o in g["items"]:
                        rows_opps.append((o["name"], o.get("deadline_short", ""), o.get("url", "")))
            if b["type"] == "essay":
                rows_reads.append((b["title"], b.get("author", ""), b.get("source_note", "").split(" · ")[0]))
            if b["type"] == "newsstand":
                for n in b["items"]:
                    if n.get("mode") != "in full" and n.get("url"):
                        rows_stand.append((n["title"], n.get("pub", ""), n["url"]))
    li = lambda x: f"<li>{x}</li>"
    a = lambda text, u: f'<a href="{html.escape(_url(u))}">{html.escape(text)}</a>' if _url(u) else html.escape(text)
    base = cfg["delivery"].get("repo_url", "").rstrip("/") + f"/blob/main/issues/{iss['date']}/"
    back = iss.get("back", {})
    credits = [f"Back page: {back.get('title', '')}. {back.get('credit', '')}"] + iss.get("credits", [])
    parts = [
        f"<p>Good morning, {html.escape(cfg['paper']['reader'])}. Today’s <b>{html.escape(cfg['paper']['name'])}</b> "
        f"(No. {html.escape(str(iss.get('number', '')))}, {html.escape(iss.get('date_long', ''))}) is ready.</p>"
        f"<p><b>{a('print-booklet.pdf', base + 'print-booklet.pdf')}</b>: print double-sided, flip on the short edge, and fold. "
        f"{a('paper.pdf', base + 'paper.pdf')}: page by page, for reading on a screen. "
        "The repository is private, so sign in to GitHub first, then press Download.</p>",
        "<h3>Needs you</h3><ol>" + "".join(li(f"<b>{html.escape(i['what'])}</b> {html.escape(i['detail'])}") for i in attention) + "</ol>",
        "<h3>Sources for today’s news</h3><ul>" + "".join(li(f"{html.escape(r)} — {a(h, u)} ({html.escape(o)}, {html.escape(d)})") for r, h, o, d, u in rows_news) + "</ul>",
        "<h3>Essays printed in full</h3><ul>" + "".join(li(f"{a(t, u)} — {html.escape(au)}") for t, au, u in rows_reads) + "</ul>",
        "<h3>Opportunity links</h3><ul>" + "".join(li(f"{a(n, u)} — {html.escape(d)}") for n, d, u in rows_opps) + "</ul>",
        *(["<h3>Newsletters summed up</h3><ul>" + "".join(li(f"{a(t, u)} — {html.escape(pb)}") for t, pb, u in rows_stand) + "</ul>"] if rows_stand else []),
        *(["<h3>Notes from the editor</h3><ul>" + "".join(li(html.escape(n)) for n in iss["email_notes"]) + "</ul>"] if iss.get("email_notes") else []),
        "<h3>Art and credits</h3><ul>" + "".join(li(html.escape(c)) for c in credits) + "</ul>",
        "<h3>House rules</h3><ul>" + "".join(li(html.escape(r)) for r in HOUSE_RULES) + "</ul>",
    ]
    body = "\n".join(parts)
    (issue_path.parent / "email.html").write_text(body)
    print(body)


if __name__ == "__main__":
    build(Path(sys.argv[1]).resolve())
