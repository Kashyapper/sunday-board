#!/usr/bin/env python3
"""Inject the ingredient table into the page and write the publishable index.html.

The source page carries a __INGREDIENT_TABLE__ placeholder so it stays editable
without 1,896 lines of data in the middle of it. This script fills that in.

    python3 src/build.py
"""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "src" / "sunday-board.html"
DATA = ROOT / "src" / "data" / "ingredients.txt"
OUT = ROOT / "index.html"

PLACEHOLDER = "__INGREDIENT_TABLE__"


def main() -> int:
    page = SRC.read_text(encoding="utf-8")
    if PLACEHOLDER not in page:
        print(f"error: {PLACEHOLDER} not found in {SRC}", file=sys.stderr)
        return 1

    rows = [
        line for line in DATA.read_text(encoding="utf-8").splitlines()
        if line and not line.startswith("#")
    ]
    table = "\n".join(rows)

    # the table is embedded in a JS template literal, so these would break it
    for bad in ("`", "${"):
        if bad in table:
            print(f"error: ingredient data contains {bad!r}", file=sys.stderr)
            return 1

    body = page.replace(PLACEHOLDER, table)

    # The artifact host wraps the page in its own skeleton, so the source has no
    # <head>. A file served from a repo or GitHub Pages needs one — without the
    # charset declaration every dash and arrow renders as mojibake.
    doc = (
        "<!doctype html>\n"
        '<html lang="en">\n'
        "<head>\n"
        '<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        "</head>\n"
        "<body>\n"
        f"{body}\n"
        "</body>\n"
        "</html>\n"
    )
    OUT.write_text(doc, encoding="utf-8")
    print(f"built {OUT.relative_to(ROOT)} — {OUT.stat().st_size // 1024} KB, "
          f"{len(rows)} base ingredients")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
