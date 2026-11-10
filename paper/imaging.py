"""Turn any photo into something that prints well on a black-and-white laser printer.

Two looks:
  halftone  -- classic newspaper dots on a 45-degree screen
  engrave   -- line-screen 'engraving' look (horizontal lines of varying weight)
Output is a 1-bit PNG at print resolution, so the printer never has to guess.
"""
from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageOps


def _prep(src: Path, width_in: float, dpi: int) -> Image.Image:
    im = Image.open(src).convert("L")
    w = int(width_in * dpi)
    h = int(im.height * w / im.width)
    im = im.resize((w, h), Image.LANCZOS)
    im = ImageOps.autocontrast(im, cutoff=1)
    return im.filter(ImageFilter.UnsharpMask(radius=2, percent=80))


def halftone(src: Path, out: Path, width_in=4.5, dpi=600, lpi=65, angle=45) -> Path:
    im = _prep(src, width_in, dpi)
    cell = dpi / lpi
    W, H = im.size
    canvas = Image.new("L", (W, H), 255)
    draw = ImageDraw.Draw(canvas)
    a = math.radians(angle)
    ca, sa = math.cos(a), math.sin(a)
    diag = int(math.hypot(W, H) / cell) + 2
    px = im.load()
    for i in range(-diag, diag):
        for j in range(-diag, diag):
            u, v = i * cell, j * cell
            x = u * ca - v * sa + W / 2
            y = u * sa + v * ca + H / 2
            if not (0 <= x < W and 0 <= y < H):
                continue
            darkness = 1 - px[int(x), int(y)] / 255
            r = cell * 0.62 * math.sqrt(darkness)
            if r > 0.35:
                draw.ellipse((x - r, y - r, x + r, y + r), fill=0)
    canvas.convert("1").save(out, dpi=(dpi, dpi))
    return out


def engrave(src: Path, out: Path, width_in=4.5, dpi=600, lpi=70) -> Path:
    im = _prep(src, width_in, dpi)
    W, H = im.size
    spacing = dpi / lpi
    canvas = Image.new("L", (W, H), 255)
    draw = ImageDraw.Draw(canvas)
    px = im.load()
    y = spacing / 2
    while y < H:
        for x in range(W):
            darkness = 1 - px[x, int(y)] / 255
            half = spacing * 0.5 * darkness
            if half > 0.3:
                draw.line((x, y - half, x, y + half), fill=0)
        y += spacing
    canvas.convert("1").save(out, dpi=(dpi, dpi))
    return out
