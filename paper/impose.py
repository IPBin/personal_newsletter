"""Booklet imposition: half-letter pages -> Letter landscape sheets, 2-up.

Print the result double-sided, "flip on short edge", fold the stack in half,
and the pages read in order. Page count must be a multiple of 4.
"""
from __future__ import annotations

from pathlib import Path

from pypdf import PageObject, PdfReader, PdfWriter, Transformation

LETTER_LANDSCAPE = (792, 612)  # points
HALF_W = 396


def booklet_order(n: int) -> list[tuple[int, int]]:
    """Return (left, right) 0-based page indices for each printed side, in print order."""
    assert n % 4 == 0, "page count must be a multiple of 4"
    sides = []
    for s in range(n // 4):
        sides.append((n - 1 - 2 * s, 2 * s))          # front of sheet s
        sides.append((2 * s + 1, n - 2 - 2 * s))      # back of sheet s
    return sides


def impose(src: Path, out: Path) -> Path:
    reader = PdfReader(str(src))
    pages = reader.pages
    writer = PdfWriter()
    for left, right in booklet_order(len(pages)):
        sheet = PageObject.create_blank_page(width=LETTER_LANDSCAPE[0], height=LETTER_LANDSCAPE[1])
        for idx, x0 in ((left, 0), (right, HALF_W)):
            p = pages[idx]
            pw = float(p.mediabox.width)
            ph = float(p.mediabox.height)
            scale = min(HALF_W / pw, LETTER_LANDSCAPE[1] / ph)
            tx = x0 + (HALF_W - pw * scale) / 2
            ty = (LETTER_LANDSCAPE[1] - ph * scale) / 2
            sheet.merge_transformed_page(p, Transformation().scale(scale).translate(tx, ty))
        writer.add_page(sheet)
    # merging copies fonts and images once per page; fold the copies back together
    writer.compress_identical_objects(remove_duplicates=True, remove_unreferenced=True)
    for page in writer.pages:
        page.compress_content_streams()
    with open(out, "wb") as f:
        writer.write(f)
    return out
