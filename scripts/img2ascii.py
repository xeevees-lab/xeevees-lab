#!/usr/bin/env python3
"""
Turn a picture into the ASCII column used by the neofetch panel.

    python scripts/img2ascii.py assets/avatar.png            # default 46 cols
    python scripts/img2ascii.py assets/avatar.png --cols 56
    python scripts/img2ascii.py --placeholder                # no photo yet

Writes assets/ascii.txt, which gen_neofetch.py reads.
"""
import argparse
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "assets", "ascii.txt")

# bright -> dark. Monospace cells are ~2x taller than wide, so we halve the rows.
RAMP = "@%#*+=-:. "
RAMP_DENSE = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "


def from_image(path, cols, ramp, invert, contrast, crop=None, aspect=0.5, mask=False):
    from PIL import Image, ImageDraw, ImageEnhance, ImageOps

    img = Image.open(path).convert("RGB")

    if crop:
        cx, cy, cw, ch = crop
        img = img.crop((cx, cy, cx + cw, cy + ch))
    else:
        # centre square, so circular avatars stay centred
        w, h = img.size
        s = min(w, h)
        img = img.crop(((w - s) // 2, (h - s) // 2, (w - s) // 2 + s, (h - s) // 2 + s))

    img = ImageOps.autocontrast(img, cutoff=2)
    img = ImageEnhance.Contrast(img).enhance(contrast)
    img = img.convert("L")

    if mask:
        # knock out everything outside a soft ellipse, so a busy background
        # doesn't drown the subject in noise
        from PIL import ImageFilter

        w, h = img.size
        m = Image.new("L", (w, h), 0)
        ImageDraw.Draw(m).ellipse(
            (w * 0.02, h * 0.02, w * 0.98, h * 0.98), fill=255
        )
        m = m.filter(ImageFilter.GaussianBlur(w * 0.05))
        img = Image.composite(img, Image.new("L", (w, h), 0), m)

    rows = max(1, int(cols * aspect))
    img = img.resize((cols, rows), Image.LANCZOS)

    px = img.load()
    lines = []
    n = len(ramp) - 1
    for y in range(rows):
        line = []
        for x in range(cols):
            v = px[x, y] / 255.0
            if invert:
                v = 1.0 - v
            line.append(ramp[int((1.0 - v) * n)])
        lines.append("".join(line).rstrip())
    return lines


def placeholder(cols):
    """An orbiting-electron glyph — stands in until a photo is supplied."""
    rows = int(cols * 0.5)
    grid = [[" "] * cols for _ in range(rows)]
    cx, cy = (cols - 1) / 2.0, (rows - 1) / 2.0
    rx, ry = cols * 0.46, rows * 0.46

    for k, ang in enumerate((0.0, math.pi / 3, 2 * math.pi / 3)):
        ch = "..:"[k]
        for t in range(2000):
            th = 2 * math.pi * t / 2000.0
            ex, ey = rx * math.cos(th), ry * 0.34 * math.sin(th)
            x = cx + ex * math.cos(ang) - ey * math.sin(ang)
            y = cy + (ex * math.sin(ang) + ey * math.cos(ang)) * 0.55
            xi, yi = int(round(x)), int(round(y))
            if 0 <= xi < cols and 0 <= yi < rows:
                grid[yi][xi] = ch

    for dy in range(-1, 2):
        for dx in range(-2, 3):
            if abs(dx) + abs(dy) * 2 <= 2:
                yi, xi = int(cy) + dy, int(cx) + dx
                if 0 <= xi < cols and 0 <= yi < rows:
                    grid[yi][xi] = "#"

    return ["".join(r).rstrip() for r in grid]


def main():
    p = argparse.ArgumentParser()
    p.add_argument("image", nargs="?")
    p.add_argument("--cols", type=int, default=46)
    p.add_argument("--dense", action="store_true", help="70-char ramp, more detail")
    p.add_argument("--invert", action="store_true", help="for light-background photos")
    p.add_argument("--contrast", type=float, default=1.4)
    p.add_argument("--crop", help="x,y,w,h in source pixels")
    p.add_argument("--aspect", type=float, default=0.5,
                   help="rows = cols * aspect; raise for portraits")
    p.add_argument("--mask", action="store_true",
                   help="soft elliptical vignette; kills a busy background")
    p.add_argument("--placeholder", action="store_true")
    a = p.parse_args()

    if a.placeholder or not a.image:
        lines = placeholder(a.cols)
    else:
        if not os.path.exists(a.image):
            sys.exit(f"no such file: {a.image}")
        crop = tuple(int(v) for v in a.crop.split(",")) if a.crop else None
        lines = from_image(
            a.image, a.cols, RAMP_DENSE if a.dense else RAMP,
            a.invert, a.contrast, crop, a.aspect, a.mask,
        )

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(f"wrote {OUT}  ({len(lines)} rows x {a.cols} cols)")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
