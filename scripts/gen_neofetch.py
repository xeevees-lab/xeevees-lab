#!/usr/bin/env python3
"""
Render the neofetch-style profile card to assets/neofetch.svg.

    python scripts/img2ascii.py assets/avatar.png    # 1. make the ascii column
    python scripts/gen_neofetch.py                   # 2. render the card

Edit scripts/config.py to change any of the text.
"""
import os
import sys
from html import escape

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import config as C  # noqa: E402

ASCII_PATH = os.path.join(ROOT, "assets", "ascii.txt")
OUT = os.path.join(ROOT, "assets", "neofetch.svg")

CW = C.FONT_SIZE * C.CHAR_W  # px advance per character


def load_art():
    if not os.path.exists(ASCII_PATH):
        return []
    with open(ASCII_PATH, encoding="utf-8") as f:
        return [ln.rstrip("\n") for ln in f if ln.strip("\n") != "" or True]


def build_panel(width):
    """Return list of rows; each row is a list of (col, text, colour)."""
    rows = []

    def blank():
        rows.append([])

    # --- header: veenus@xeevees ───────────────────────
    title = f"{C.USER}@{C.HOST}"
    rows.append([
        (0, title, C.ACCENT),
        (len(title) + 1, "─" * max(0, width - len(title) - 1), C.BORDER),
    ])
    blank()

    def kv_row(indent, key, value, avail):
        if key == "" and value == "":
            blank()
            return
        label = f"{key}:"
        dots = max(1, avail - len(label) - len(value))
        rows.append([
            (indent, label, C.KEY),
            (indent + len(label), "." * dots, C.BORDER),
            (indent + len(label) + dots, value, C.FG),
        ])

    for idx, (heading, items) in enumerate(C.SECTIONS):
        if heading is None:
            for k, v in items:
                kv_row(1, k, v, width - 3)
        else:
            if idx:
                blank()
            cap = f"╭─ {heading} "
            rows.append([
                (0, cap, C.ACCENT),
                (len(cap), "─" * max(0, width - len(cap) - 1), C.BORDER),
                (width - 1, "╮", C.BORDER),
            ])
            for k, v in items:
                inner = width - 4
                if k == "" and v == "":
                    rows.append([(0, "│", C.BORDER), (width - 1, "│", C.BORDER)])
                    continue
                label = f"{k}:"
                dots = max(1, inner - len(label) - len(v))
                rows.append([
                    (0, "│", C.BORDER),
                    (2, label, C.KEY),
                    (2 + len(label), "." * dots, C.BORDER),
                    (2 + len(label) + dots, v, C.FG),
                    (width - 1, "│", C.BORDER),
                ])
            rows.append([(0, "╰" + "─" * (width - 2) + "╯", C.BORDER)])

    return rows


def main():
    art = load_art()
    art_w = max((len(l) for l in art), default=0)
    panel_x = art_w + (C.GAP if art_w else 0)

    panel_w = getattr(C, "PANEL_W", 66)
    rows = build_panel(panel_w)

    total_cols = panel_x + panel_w
    total_rows = max(len(art), len(rows))

    w = int(round(total_cols * CW + 2 * C.PAD))
    h = int(round(total_rows * C.LINE_H + 2 * C.PAD))

    def x(col):
        return round(C.PAD + col * CW, 2)

    def y(row):
        return round(C.PAD + (row + 0.8) * C.LINE_H, 2)

    def text_el(col, row, s, colour):
        """One run, pinned to an exact width.

        GitHub renders this SVG with whatever monospace font its image pipeline
        happens to have, and that font's advance width is not necessarily the
        CHAR_W we laid the grid out on. Without textLength the difference
        accumulates across long runs — dot leaders drift, and the ascii art
        visibly shears. textLength forces every run into its allotted box, so
        the card looks the same in any renderer.
        """
        attrs = ""
        if len(s) > 1:
            attrs = f' textLength="{round(len(s) * CW, 2)}" lengthAdjust="spacing"'
        return (
            f'<text x="{x(col)}" y="{y(row)}" fill="{colour}"{attrs}>'
            f"{escape(s)}</text>"
        )

    out = []
    out.append(
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
        f'viewBox="0 0 {w} {h}" font-family="ui-monospace,\'JetBrains Mono\','
        f"'DejaVu Sans Mono','Liberation Mono',Menlo,Consolas,monospace\" "
        f'font-size="{C.FONT_SIZE}" xml:space="preserve">'
    )
    out.append(f'<rect width="{w}" height="{h}" rx="14" fill="{C.BG}"/>')
    out.append(
        f'<rect x="0.5" y="0.5" width="{w-1}" height="{h-1}" rx="13.5" '
        f'fill="none" stroke="{C.BORDER}" stroke-opacity="0.6"/>'
    )

    # ascii column
    off = max(0, (total_rows - len(art)) // 2)
    for i, line in enumerate(art):
        if not line.strip():
            continue
        out.append(text_el(0, i + off, line, C.ART))

    # info panel
    for i, runs in enumerate(rows):
        for col, text, colour in runs:
            if not text:
                continue
            out.append(text_el(panel_x + col, i, text, colour))

    out.append("</svg>")

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    print(f"wrote {OUT}  ({w}x{h}px, {total_cols} cols x {total_rows} rows)")


if __name__ == "__main__":
    main()
