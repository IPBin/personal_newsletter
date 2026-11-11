"""Quercus (Canvas) reader: assignments and calendar items with due dates.

Quercus blocks outside apps, but every Canvas account has a private calendar feed
(Calendar → "Calendar Feed", bottom right). It lists every published assignment,
quiz and course event with its due date and time. The feed address is a secret:
it is read from the QUERCUS_ICAL_URL environment variable and nowhere else.
Never write it into a file, a commit, the paper or an email.

  python collectors/quercus.py                  # print JSON
  python collectors/quercus.py out/quercus.json

What the feed does NOT have: announcements (those arrive by Gmail, label Quercus),
syllabus files, grades, and anything a professor has not published yet.
"""
from __future__ import annotations

import datetime as dt
import json
import os
import re
import sys
from zoneinfo import ZoneInfo

import requests

TZ = ZoneInfo("America/Toronto")


def _unfold(text: str) -> list[str]:
    return re.sub(r"\r?\n[ \t]", "", text).splitlines()


def _when(value: str, params: str):
    """Return (iso string in Toronto time, all_day)."""
    if re.fullmatch(r"\d{8}", value):
        return dt.date(int(value[:4]), int(value[4:6]), int(value[6:])).isoformat(), True
    t = dt.datetime.strptime(value.rstrip("Z"), "%Y%m%dT%H%M%S")
    if value.endswith("Z"):
        t = t.replace(tzinfo=dt.timezone.utc)
    else:
        m = re.search(r"TZID=([^;:]+)", params)
        t = t.replace(tzinfo=ZoneInfo(m.group(1)) if m else TZ)
    return t.astimezone(TZ).isoformat(timespec="minutes"), False


def parse(ics: str) -> list[dict]:
    out, cur = [], None
    for line in _unfold(ics):
        if line == "BEGIN:VEVENT":
            cur = {}
        elif line == "END:VEVENT" and cur is not None:
            out.append(cur)
            cur = None
        elif cur is not None and ":" in line:
            key, value = line.split(":", 1)
            name, _, params = key.partition(";")
            value = value.replace("\\n", " ").replace("\\,", ",").replace("\\;", ";").strip()
            if name == "SUMMARY":
                m = re.match(r"(.*)\s\[(.+)\]$", value)      # Canvas puts the course in [brackets]
                cur["title"], cur["course"] = (m.group(1), m.group(2)) if m else (value, None)
            elif name == "DTSTART":
                cur["due"], cur["all_day"] = _when(value, params)
            elif name == "URL":
                cur["url"] = value
            elif name == "UID":
                cur["kind"] = "assignment" if "assignment" in value else "event"
                cur["uid"] = value
    return out


def fetch(url: str | None = None, days_back: int = 14, days_ahead: int = 60) -> dict:
    url = url or os.environ.get("QUERCUS_ICAL_URL")
    if not url:
        return {"error": "QUERCUS_ICAL_URL is not set"}
    try:
        r = requests.get(url.replace("webcal://", "https://"), timeout=30)
        r.raise_for_status()
    except Exception as e:   # report the kind of failure, never the address
        return {"error": type(e).__name__}
    today = dt.datetime.now(TZ).date()
    lo, hi = today - dt.timedelta(days=days_back), today + dt.timedelta(days=days_ahead)
    items = [i for i in parse(r.text) if i.get("due") and lo.isoformat() <= i["due"][:10] <= hi.isoformat()]
    items.sort(key=lambda i: i["due"])
    return {"fetched": dt.datetime.now(TZ).isoformat(timespec="seconds"), "items": items}


if __name__ == "__main__":
    text = json.dumps(fetch(), indent=1, ensure_ascii=False)
    if len(sys.argv) > 1:
        os.makedirs(os.path.dirname(sys.argv[1]) or ".", exist_ok=True)
        open(sys.argv[1], "w").write(text)
    else:
        print(text)
