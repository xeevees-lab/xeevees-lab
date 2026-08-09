#!/usr/bin/env python3
"""
Local sanity-render of assets/neofetch.svg -> _preview.png.

Honours textLength/lengthAdjust the same way a real SVG renderer does — each
run is laid out into its declared box — so the preview shows what GitHub will
show even though the fonts differ. Not needed for GitHub; purely a check.

    python scripts/preview.py            # default font
    python scripts/preview.py --font 13  # simulate a narrower/wider font
"""
import argparse
import html
import os
import re

from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"

RUN = re.compile(
    r'<text x="([\d.]+)" y="([\d.]+)" fill="(#\w+)"'
    r'(?: textLength="([\d.]+)" lengthAdjust="spacing")?>(.*?)</text>',
    re.S,
)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--font", type=int, default=15,
                    help="render size; vary it to prove alignment is font-proof")
    a = ap.parse_args()

    svg = open(os.path.join(ROOT, "assets", "neofetch.svg"), encoding="utf-8").read()
    w = int(re.search(r'width="(\d+)"', svg).group(1))
    h = int(re.search(r'height="(\d+)"', svg).group(1))
    bg = re.search(r'<rect width[^>]*fill="(#\w+)"', svg).group(1)

    im = Image.new("RGB", (w, h), bg)
    d = ImageDraw.Draw(im)
    f = ImageFont.truetype(FONT, a.font)

    n = 0
    for m in RUN.finditer(svg):
        x, y, colour, tlen, s = m.groups()
        x, y = float(x), float(y)
        s = html.unescape(s)
        if tlen and len(s) > 1:
            step = float(tlen) / len(s)          # lengthAdjust="spacing"
            for i, ch in enumerate(s):
                d.text((x + i * step, y), ch, font=f, fill=colour, anchor="ls")
        else:
            d.text((x, y), s, font=f, fill=colour, anchor="ls")
        n += 1

    out = os.path.join(ROOT, "_preview.png")
    im.save(out)
    print(f"wrote _preview.png  {w}x{h}  ({n} runs, font size {a.font})")


if __name__ == "__main__":
    main()
