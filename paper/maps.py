"""Small black-and-white locator maps drawn from world-atlas TopoJSON.

No network, no GIS stack: decode TopoJSON arcs ourselves and project with a
simple equirectangular projection scaled by cos(latitude). Good enough for
print-sized locator maps.
"""
from __future__ import annotations

import json
import math
from functools import lru_cache
from pathlib import Path

GEO = Path(__file__).resolve().parent.parent / "assets" / "geo"

# ISO 3166-1 numeric ids used by world-atlas
COUNTRY_IDS = {
    "indonesia": "360",
    "canada": "124",
    "usa": "840",
    "united states": "840",
    "malaysia": "458",
    "australia": "036",
    "mexico": "484",
    "china": "156",
    "india": "356",
    "uk": "826",
    "japan": "392",
}


@lru_cache(maxsize=2)
def _topology(res: str = "50m"):
    with open(GEO / f"countries-{res}.json") as f:
        topo = json.load(f)
    sx, sy = topo["transform"]["scale"]
    tx, ty = topo["transform"]["translate"]
    arcs = []
    for arc in topo["arcs"]:
        x = y = 0
        pts = []
        for dx, dy in arc:
            x += dx
            y += dy
            pts.append((x * sx + tx, y * sy + ty))
        arcs.append(pts)
    return topo, arcs


def _ring(arcs, idxs):
    pts = []
    for i in idxs:
        a = arcs[i] if i >= 0 else list(reversed(arcs[~i]))
        pts.extend(a if not pts else a[1:])
    return pts


def _country_polys(res="50m"):
    topo, arcs = _topology(res)
    out = {}
    for g in topo["objects"]["countries"]["geometries"]:
        cid = str(g.get("id", ""))
        polys = []
        if g["type"] == "Polygon":
            polys.append([_ring(arcs, r) for r in g["arcs"]])
        elif g["type"] == "MultiPolygon":
            for p in g["arcs"]:
                polys.append([_ring(arcs, r) for r in p])
        out.setdefault(cid, []).extend(polys)
    return out


def locator_map(
    focus: str,
    bbox: tuple[float, float, float, float],
    points: list[dict] | None = None,
    width: float = 300,
    res: str = "50m",
    title: str | None = None,
) -> str:
    """Return an SVG string.

    focus  -- country key (see COUNTRY_IDS) drawn with a hatched fill
    bbox   -- (lon_min, lat_min, lon_max, lat_max)
    points -- [{"lon":..,"lat":..,"label":..,"anchor":"start|end"}]
    """
    focus_id = COUNTRY_IDS.get(focus.lower(), focus)
    lon0, lat0, lon1, lat1 = bbox
    k = math.cos(math.radians((lat0 + lat1) / 2))
    w_units = (lon1 - lon0) * k
    h_units = lat1 - lat0
    height = width * h_units / w_units

    def proj(lon, lat):
        return ((lon - lon0) * k / w_units * width, (lat1 - lat) / h_units * height)

    polys = _country_polys(res)
    paths_bg, paths_fg = [], []
    for cid, plist in polys.items():
        for poly in plist:
            d = []
            inside = False
            for ring in poly:
                if not ring:
                    continue
                # cheap cull
                if any(lon0 - 5 <= x <= lon1 + 5 and lat0 - 5 <= y <= lat1 + 5 for x, y in ring[:: max(1, len(ring) // 20)]):
                    inside = True
                seg = []
                for i, (x, y) in enumerate(ring):
                    px, py = proj(x, y)
                    seg.append(("M" if i == 0 else "L") + f"{px:.1f},{py:.1f}")
                d.append("".join(seg) + "Z")
            if not inside or not d:
                continue
            (paths_fg if cid == focus_id else paths_bg).append(" ".join(d))

    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width:.0f} {height:.0f}" '
        f'width="{width:.0f}" height="{height:.0f}" class="map">',
        "<defs><pattern id='hatch' width='3' height='3' patternUnits='userSpaceOnUse' "
        "patternTransform='rotate(45)'><line x1='0' y1='0' x2='0' y2='3' stroke='#000' stroke-width='0.9'/></pattern>"
        f"<clipPath id='clip'><rect x='0' y='0' width='{width:.0f}' height='{height:.0f}'/></clipPath></defs>",
        "<g clip-path='url(#clip)'>",
    ]
    for d in paths_bg:
        svg.append(f"<path d='{d}' fill='#fff' stroke='#555' stroke-width='0.4'/>")
    for d in paths_fg:
        svg.append(f"<path d='{d}' fill='#bdbdbd' stroke='#000' stroke-width='0.6'/>")
    svg.append("</g>")
    for p in points or []:
        x, y = proj(p["lon"], p["lat"])
        svg.append(f"<circle cx='{x:.1f}' cy='{y:.1f}' r='3.2' fill='#fff' stroke='#000' stroke-width='1.2'/>")
        svg.append(f"<circle cx='{x:.1f}' cy='{y:.1f}' r='1.2' fill='#000'/>")
        anchor = p.get("anchor", "start")
        dx = 6 if anchor == "start" else -6
        svg.append(
            f"<text x='{x + dx:.1f}' y='{y + 3:.1f}' text-anchor='{anchor}' "
            "font-family='IBM Plex Sans Condensed' font-size='8.5' font-weight='600' fill='#000'>"
            f"{_esc(p['label'])}</text>"
        )
    svg.append(f"<rect x='0.5' y='0.5' width='{width - 1:.0f}' height='{height - 1:.0f}' fill='none' stroke='#000' stroke-width='0.6'/>")
    if title:
        svg.append(
            f"<text x='6' y='{height - 6:.0f}' font-family='IBM Plex Sans Condensed' font-size='7.5' "
            "letter-spacing='1' paint-order='stroke' stroke='#fff' stroke-width='2.5'>"
            f"{_esc(title.upper())}</text>"
        )
    svg.append("</svg>")
    return "\n".join(svg)


def _esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


# Ready-made views for the regions the paper covers.
VIEWS = {
    "indonesia": {"focus": "indonesia", "bbox": (94.0, -11.5, 141.5, 6.5)},
    "canada": {"focus": "canada", "bbox": (-141.0, 41.0, -52.0, 70.0)},
    "usa": {"focus": "usa", "bbox": (-125.0, 24.0, -66.0, 50.0)},
}


def region_map(region: str, points=None, width=300, title=None) -> str:
    v = VIEWS[region]
    return locator_map(v["focus"], v["bbox"], points=points, width=width, title=title)
