"""Cloud fetcher — runs on GitHub Actions every morning before the paper is written.

Claude's own sandbox can only reach a short allow-list of hosts, so anything that
needs the open web is fetched here and committed to `collected/<date>/` for the
morning run to read:

  news.json           recent items from the RSS feeds in collectors/feeds.yaml
  watch/<slug>.txt    plain text of each opportunity watch page + changed flag
  luma_toronto.json   upcoming public Luma events in Toronto (best effort)
  todoist.json        open Todoist tasks (needs the TODOIST_TOKEN repo secret)
  photo/              Wikimedia Commons picture of the day, converted to halftone

NOTE: written during setup but not yet run — the first Actions run is its test.
"""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import os
import re
import sys
from pathlib import Path

import feedparser
import requests
import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
TODAY = dt.date.today().isoformat()
OUT = ROOT / "collected" / TODAY
UA = {"User-Agent": "the-long-view/0.1 (personal newspaper; github actions)"}


def get(url, **kw):
    r = requests.get(url, headers=UA, timeout=25, **kw)
    r.raise_for_status()
    return r


def news():
    feeds = yaml.safe_load(open(ROOT / "collectors" / "feeds.yaml"))
    cutoff = dt.datetime.now(dt.timezone.utc) - dt.timedelta(hours=36)
    out = {}
    for region, urls in feeds.items():
        items = []
        for url in urls:
            try:
                f = feedparser.parse(get(url).content)
            except Exception as e:  # keep going; report the failure
                items.append({"error": f"{url}: {e}"})
                continue
            for e in f.entries[:25]:
                t = e.get("published_parsed") or e.get("updated_parsed")
                when = dt.datetime(*t[:6], tzinfo=dt.timezone.utc) if t else None
                if when and when < cutoff:
                    continue
                items.append({
                    "source": f.feed.get("title", url), "title": e.get("title"),
                    "url": e.get("link"), "published": when.isoformat() if when else None,
                    "summary": re.sub("<[^>]+>", "", e.get("summary", ""))[:1200],
                })
        out[region] = items
    (OUT / "news.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))


def watch_pages():
    cfg = yaml.safe_load(open(ROOT / "config.yaml"))
    urls = cfg["opportunities"]["aggregators"] + cfg["opportunities"]["watch_pages"]
    wdir = OUT / "watch"
    wdir.mkdir(parents=True, exist_ok=True)
    hashes_path = ROOT / "state" / "watch_hashes.json"
    hashes = json.loads(hashes_path.read_text()) if hashes_path.exists() else {}
    index = []
    for url in urls:
        slug = re.sub(r"[^a-z0-9]+", "-", url.lower())[8:80]
        try:
            html = get(url).text
        except Exception as e:
            index.append({"url": url, "error": str(e)})
            continue
        text = re.sub(r"(?is)<(script|style|noscript).*?</\1>", " ", html)
        text = re.sub(r"<[^>]+>", " ", text)
        text = re.sub(r"\s+", " ", text).strip()
        h = hashlib.sha256(text.encode()).hexdigest()
        changed = hashes.get(url) != h
        hashes[url] = h
        (wdir / f"{slug}.txt").write_text(text[:60000])
        index.append({"url": url, "file": f"watch/{slug}.txt", "changed": changed})
    (OUT / "watch_index.json").write_text(json.dumps(index, indent=1))
    hashes_path.write_text(json.dumps(hashes, indent=1))


def luma_toronto():
    # Public discover endpoint used by luma.com/toronto; unofficial, so best effort.
    try:
        r = get("https://api.lu.ma/discover/get-paginated-events",
                params={"discover_place_api_id": "discplace-toronto", "pagination_limit": 50})
        evs = []
        for e in r.json().get("entries", []):
            ev = e.get("event", {})
            evs.append({"name": ev.get("name"), "start": ev.get("start_at"),
                        "url": "https://luma.com/" + ev.get("url", ""),
                        "where": (ev.get("geo_address_info") or {}).get("full_address")})
        (OUT / "luma_toronto.json").write_text(json.dumps(evs, indent=1, ensure_ascii=False))
    except Exception as e:
        (OUT / "luma_toronto.json").write_text(json.dumps({"error": str(e)}))


def todoist():
    token = os.environ.get("TODOIST_TOKEN")
    if not token:
        return
    h = {**UA, "Authorization": f"Bearer {token}"}
    try:
        tasks = requests.get("https://api.todoist.com/rest/v2/tasks", headers=h, timeout=25).json()
        projects = {p["id"]: p["name"] for p in requests.get("https://api.todoist.com/rest/v2/projects", headers=h, timeout=25).json()}
        slim = [{"content": t["content"], "project": projects.get(t["project_id"]),
                 "due": (t.get("due") or {}).get("date"), "priority": t.get("priority"),
                 "labels": t.get("labels")} for t in tasks]
        (OUT / "todoist.json").write_text(json.dumps(slim, indent=1, ensure_ascii=False))
    except Exception as e:
        (OUT / "todoist.json").write_text(json.dumps({"error": str(e)}))


def picture_of_the_day():
    from paper.imaging import halftone
    d = dt.date.today()
    try:
        r = get(f"https://api.wikimedia.org/feed/v1/wikipedia/en/featured/{d:%Y/%m/%d}").json()
        img = r.get("image") or {}
        src = (img.get("thumbnail") or {}).get("source")
        if not src:
            return
        pdir = OUT / "photo"
        pdir.mkdir(exist_ok=True)
        raw = pdir / "original.jpg"
        raw.write_bytes(get(src).content)
        halftone(raw, pdir / "halftone.png")
        meta = {"title": img.get("title"), "description": (img.get("description") or {}).get("text"),
                "artist": (img.get("artist") or {}).get("text"), "license": (img.get("license") or {}).get("type"),
                "page": img.get("file_page")}
        (pdir / "meta.json").write_text(json.dumps(meta, indent=1, ensure_ascii=False))
    except Exception as e:
        print("photo:", e)


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for step in (news, watch_pages, luma_toronto, todoist, picture_of_the_day):
        try:
            step()
        except Exception as e:
            print(f"{step.__name__} failed: {e}")
