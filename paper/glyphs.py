"""Hand-drawn-feeling black-and-white glyphs: weather icons and a deadline ruler."""
from __future__ import annotations

import math
from datetime import date


def _svg(w, h, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">'
            f'{body}</svg>')


def _sun(cx, cy, r):
    rays = []
    for i in range(8):
        a = i * math.pi / 4
        rays.append(f"<line x1='{cx + math.cos(a) * (r + 2):.1f}' y1='{cy + math.sin(a) * (r + 2):.1f}' "
                    f"x2='{cx + math.cos(a) * (r + 5):.1f}' y2='{cy + math.sin(a) * (r + 5):.1f}' "
                    "stroke='#000' stroke-width='1.1' stroke-linecap='round'/>")
    return f"<circle cx='{cx}' cy='{cy}' r='{r}' fill='#fff' stroke='#000' stroke-width='1.1'/>" + "".join(rays)


def _cloud(x, y, s=1.0, fill="#fff"):
    return (f"<g transform='translate({x},{y}) scale({s})'>"
            f"<path d='M4,14 Q0,14 0,10 Q0,6 5,6 Q6,1 12,1 Q18,1 19,6 Q25,6 25,10 Q25,14 21,14 Z' "
            f"fill='{fill}' stroke='#000' stroke-width='1.1' stroke-linejoin='round'/></g>")


def weather_icon(kind: str, size=30) -> str:
    kind = (kind or "").lower()
    b = []
    if "snow" in kind:
        b.append(_cloud(2, 3))
        for x in (8, 14, 20):
            b.append(f"<text x='{x}' y='27' font-size='8' text-anchor='middle' font-family='IBM Plex Sans Condensed'>*</text>")
    elif "rain" in kind and "chance" not in kind:
        b.append(_cloud(2, 3))
        for x in (8, 14, 20):
            b.append(f"<line x1='{x}' y1='20' x2='{x - 2}' y2='26' stroke='#000' stroke-width='1.1' stroke-linecap='round'/>")
    elif "cloud" in kind and "part" in kind or "mostly" in kind:
        b.append(_sun(19, 10, 5))
        b.append(_cloud(1, 9))
    elif "cloud" in kind:
        b.append(_cloud(2, 7))
    else:
        b.append(_sun(15, 15, 6))
    return _svg(size, size, "".join(b))


def day_kind(day: dict) -> str:
    pc = day.get("precipitation_chance", 0) or 0
    pt = day.get("precipitation_type", "rain")
    if pc >= 40:
        return pt or "partly cloudy"   # likely wet, but the forecast gave no type
    if pc >= 20:
        return "partly cloudy"
    return "sun"


def deadline_ruler(items: list[dict], today: date, days: int = 30, width=330, height=None) -> str:
    """A horizontal 'tape measure' of upcoming deadlines.

    items: [{"label": str, "date": date}]
    """
    rows = [it for it in items if it.get("date") and 0 <= (it["date"] - today).days <= days]
    rows.sort(key=lambda it: it["date"])
    # stack labels in lanes to avoid collisions
    lane_h = 11
    lanes_end: list[float] = []
    placed = []
    pad_l, pad_r = 4, 4
    span = width - pad_l - pad_r

    def x_of(d):
        return pad_l + (d - today).days / days * span

    for it in rows:
        x = x_of(it["date"])
        text_w = 4.1 * len(it["label"]) + 6
        lane = 0
        while lane < len(lanes_end) and lanes_end[lane] > x - 1:
            lane += 1
        if lane == len(lanes_end):
            lanes_end.append(0)
        lanes_end[lane] = x + text_w
        placed.append((it, x, lane))
    nl = max(1, len(lanes_end))
    axis_y = 18
    h = height or axis_y + 8 + nl * lane_h + 4
    b = [f"<line x1='{pad_l}' y1='{axis_y}' x2='{width - pad_r}' y2='{axis_y}' stroke='#000' stroke-width='1.2'/>"]
    for dd in range(0, days + 1):
        x = pad_l + dd / days * span
        major = dd % 7 == 0
        b.append(f"<line x1='{x:.1f}' y1='{axis_y - (5 if major else 2.5)}' x2='{x:.1f}' y2='{axis_y}' stroke='#000' stroke-width='{0.9 if major else 0.5}'/>")
        if major:
            d = date.fromordinal(today.toordinal() + dd)
            lbl = "today" if dd == 0 else d.strftime("%b %-d")
            anchor = "start" if dd == 0 else ("end" if dd == days else "middle")
            b.append(f"<text x='{x:.1f}' y='{axis_y - 8}' font-size='7' text-anchor='{anchor}' font-family='IBM Plex Sans Condensed'>{lbl}</text>")
    for it, x, lane in placed:
        y = axis_y + 10 + lane * lane_h
        b.append(f"<line x1='{x:.1f}' y1='{axis_y}' x2='{x:.1f}' y2='{y - 3}' stroke='#000' stroke-width='0.5' stroke-dasharray='1,1.2'/>")
        b.append(f"<circle cx='{x:.1f}' cy='{axis_y}' r='2' fill='#000'/>")
        lbl = it["label"].replace("&", "&amp;").replace("<", "&lt;")
        b.append(f"<text x='{x + 1.5:.1f}' y='{y + 3}' font-size='7.2' font-family='IBM Plex Sans Condensed'>{lbl}</text>")
    return _svg(width, h, "".join(b))


def _e(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def bar_chart(rows, width=318, unit="", max_value=None, label_w=92, bar_h=11, gap=6, note=None):
    """Horizontal bars. rows: [{"label":..., "value":..., "text": optional value label, "style": "solid|grey|outline"}]"""
    mv = max_value or max(r["value"] for r in rows) or 1
    span = width - label_w - 34
    h = len(rows) * (bar_h + gap) + 4
    b = []
    for i, r in enumerate(rows):
        y = 2 + i * (bar_h + gap)
        w = max(1.5, r["value"] / mv * span)
        fill = {"solid": "#000", "grey": "#9a9a9a", "outline": "#fff"}.get(r.get("style", "solid"), "#000")
        b.append(f"<text x='{label_w - 5}' y='{y + bar_h - 2.5}' text-anchor='end' font-size='7.8' font-family='IBM Plex Sans Condensed'>{_e(r['label'])}</text>")
        b.append(f"<rect x='{label_w}' y='{y}' width='{w:.1f}' height='{bar_h}' fill='{fill}' stroke='#000' stroke-width='0.6'/>")
        b.append(f"<text x='{label_w + w + 4:.1f}' y='{y + bar_h - 2.5}' font-size='7.8' font-weight='600' font-family='IBM Plex Sans Condensed'>{_e(r.get('text', str(r['value']) + unit))}</text>")
    return _svg(width, h, "".join(b))


def split_bar(parts, total=None, width=318, height=16, label=None):
    """One stacked bar, e.g. seats. parts: [{"name":..,"value":..,"style":"solid|grey|outline"}]"""
    total = total or sum(p["value"] for p in parts)
    x = 0.0
    b = []
    top = 11 if label else 0
    if label:
        b.append(f"<text x='0' y='8' font-size='7.6' font-weight='600' font-family='IBM Plex Sans Condensed' letter-spacing='0.6'>{_e(label.upper())}</text>")
    for p in parts:
        w = p["value"] / total * width
        fill = {"solid": "#000", "grey": "#9a9a9a", "outline": "#fff"}[p.get("style", "solid")]
        b.append(f"<rect x='{x:.1f}' y='{top}' width='{w:.1f}' height='{height}' fill='{fill}' stroke='#000' stroke-width='0.6'/>")
        tcol = "#fff" if p.get("style", "solid") == "solid" else "#000"
        if w > 34:
            b.append(f"<text x='{x + 4:.1f}' y='{top + height - 4.5}' font-size='7.6' font-weight='600' fill='{tcol}' font-family='IBM Plex Sans Condensed'>{_e(p['name'])} {p['value']}</text>")
        x += w
    # majority line
    if total:
        mid = width / 2
        b.append(f"<line x1='{mid:.1f}' y1='{top - 2}' x2='{mid:.1f}' y2='{top + height + 2}' stroke='#000' stroke-width='0.8' stroke-dasharray='2,1.5'/>")
    return _svg(width, top + height + 3, "".join(b))
