"""Todoist reader: open tasks, grouped the way the front page wants them.

The API key is read from the TODOIST_TOKEN environment variable and nowhere
else. Never write the key into a file, a commit, the paper or an email.

  python collectors/todoist.py                 # print JSON
  python collectors/todoist.py out/todoist.json

Runs in two places: the GitHub Action (repo secret TODOIST_TOKEN) and the
morning session, if api.todoist.com is allowed by the environment's network
settings and TODOIST_TOKEN is set as an environment variable there.
"""
from __future__ import annotations

import datetime as dt
import json
import os
import sys

import requests

API = "https://api.todoist.com/api/v1"
LEGACY = "https://api.todoist.com/rest/v2"   # older API, tried only as a fallback


def _all(path: str, headers: dict) -> list:
    """Read every page of a v1 list endpoint ({results, next_cursor})."""
    items, cursor = [], None
    while True:
        params = {"limit": 200, **({"cursor": cursor} if cursor else {})}
        r = requests.get(f"{API}/{path}", headers=headers, params=params, timeout=25)
        r.raise_for_status()
        data = r.json()
        if isinstance(data, list):          # unpaginated answer
            return data
        items += data.get("results", [])
        cursor = data.get("next_cursor")
        if not cursor:
            return items


def _legacy(path: str, headers: dict) -> list:
    r = requests.get(f"{LEGACY}/{path}", headers=headers, timeout=25)
    r.raise_for_status()
    return r.json()


def fetch(token: str | None = None, days_ahead: int = 3) -> dict:
    token = token or os.environ.get("TODOIST_TOKEN")
    if not token:
        return {"error": "TODOIST_TOKEN is not set"}
    h = {"Authorization": f"Bearer {token}"}
    try:
        try:
            tasks, projects = _all("tasks", h), _all("projects", h)
        except requests.HTTPError as e:
            if e.response is not None and e.response.status_code in (401, 403):
                raise
            tasks, projects = _legacy("tasks", h), _legacy("projects", h)
    except Exception as e:  # report the kind of failure, never the key
        return {"error": f"{type(e).__name__}: {str(e).replace(token, '***')}"}

    names = {p["id"]: p["name"] for p in projects}
    today = dt.date.today()
    horizon = today + dt.timedelta(days=days_ahead)
    out = []
    for t in tasks:
        if t.get("checked") or t.get("is_completed"):
            continue
        due = ((t.get("due") or {}).get("date") or "")[:10] or None
        when = None
        if due:
            d = dt.date.fromisoformat(due)
            when = "overdue" if d < today else "today" if d == today else "soon" if d <= horizon else "later"
        out.append({
            "content": t.get("content"),
            "project": names.get(t.get("project_id")),
            "due": due, "when": when,
            "priority": t.get("priority"),      # 4 = most urgent in Todoist's API
            "labels": t.get("labels") or [],
        })
    order = {"overdue": 0, "today": 1, "soon": 2, "later": 3, None: 4}
    out.sort(key=lambda t: (order[t["when"]], -(t["priority"] or 1), t["due"] or "9999"))
    return {"fetched": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"), "tasks": out}


if __name__ == "__main__":
    text = json.dumps(fetch(), indent=1, ensure_ascii=False)
    if len(sys.argv) > 1:
        os.makedirs(os.path.dirname(sys.argv[1]) or ".", exist_ok=True)
        open(sys.argv[1], "w").write(text)
    else:
        print(text)
