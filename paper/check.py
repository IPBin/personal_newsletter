"""Cheap page check after a build: one line per page, plus contact sheets to look at.

    python -m paper.check issues/2026-11-12

Prints page count, file sizes and words per page (a page far below ~300 words is
probably part blank), and writes preview/sheet-1.png … (six pages per image) so
the whole paper can be checked in four images instead of twenty.
"""
import subprocess
import sys
from pathlib import Path

from PIL import Image


def main(folder):
    d = Path(folder)
    pdf = d / "paper.pdf"
    n = int(next(l.split()[1] for l in subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True).stdout.splitlines() if l.startswith("Pages")))
    print(f"pages: {n} {'OK' if n == 20 else 'WRONG, must be 20'}")
    for f in ("paper.pdf", "print-booklet.pdf"):
        p = d / f
        size = p.stat().st_size / 1e6 if p.exists() else 0
        print(f"{f}: {size:.2f} MB {'OK' if 0 < size < 1.5 else 'CHECK (missing or over 1.5 MB)'}")
    for i in range(1, n + 1):
        text = subprocess.run(["pdftotext", "-f", str(i), "-l", str(i), str(pdf), "-"], capture_output=True, text=True).stdout
        words = len(text.split())
        first = next((l.strip() for l in text.splitlines() if len(l.strip()) > 12), "")[:60]
        flag = "" if words >= 280 or i in (1, n) else "  <- thin page, look at it"
        print(f"p{i:>2}: {words:>4} words | {first}{flag}")
    pages = sorted((d / "preview").glob("page-*.png"))
    for k in range(0, len(pages), 6):
        ims = [Image.open(p) for p in pages[k:k + 6]]
        w, h = ims[0].size
        sheet = Image.new("RGB", (w * 3, h * 2), "white")
        for j, im in enumerate(ims):
            sheet.paste(im, ((j % 3) * w, (j // 3) * h))
        out = d / "preview" / f"sheet-{k // 6 + 1}.png"
        sheet.save(out)
        print("wrote", out)


if __name__ == "__main__":
    main(sys.argv[1])
