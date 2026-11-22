#!/usr/bin/env python3
"""Copy the paper's tables into slides.md as appendix slides, one table per slide.

Written 2026-11-21 for the EVT/WOTE 2026 talk. The paper (its Markdown
sections, paper/sections/0*.md, given with --paper) has no figures; its results are five Markdown tables, each with
a "Table: caption \\label{...}" line. For each, this writes a slide with the table (in a
smaller font, class paper-table) and puts the caption and the paper's own explanation (the
paragraph before the table, or after it when the one before is only a heading) in the
speaker notes. The slides go between the markers below at the end of slides.md, replacing
whatever was there, so re-running it after the paper changes refreshes them. Standard
library only.
"""

import argparse
import re
from pathlib import Path



def _paper_sections() -> Path:
    """The paper's paper/sections folder, from the required --paper option."""
    parser = argparse.ArgumentParser(description="Copy the paper's tables into slides.md.")
    parser.add_argument("--paper", type=Path, required=True, help="the paper's paper/sections folder")
    return parser.parse_args().paper


PAPER = _paper_sections() if __name__ == "__main__" else Path(".")
SLIDES = Path(__file__).with_name("slides.md")
START, END = "<!-- paper tables: start (make_paper_slides.py) -->", "<!-- paper tables: end -->"


def paragraph(lines: list[str], i: int, step: int) -> str:
    """The paragraph next to line i, going backwards (step -1) or forwards (step 1)."""
    k = i
    while 0 <= k < len(lines) and not lines[k].strip():
        k += step
    block = []
    while 0 <= k < len(lines) and lines[k].strip():
        block.append(lines[k])
        k += step
    if step < 0:
        block.reverse()
    return " ".join(x.strip() for x in block)


def tables() -> list[tuple[str, str, str, str]]:
    """(section file, table text, caption, explanation) for each table, in the paper's order."""
    out = []
    for f in sorted(PAPER.glob("0*.md")):
        lines = f.read_text(encoding="utf-8").split("\n")
        for i, line in enumerate(lines):
            if not line.startswith("Table:"):
                continue
            end = i - 1
            while not lines[end].startswith("|"):
                end -= 1
            start = end
            while start > 0 and lines[start - 1].startswith("|"):
                start -= 1
            caption = re.sub(r"\s*\\label\{[^}]*\}", "", line[len("Table:"):]).strip()
            before = paragraph(lines, start - 1, -1)
            explanation = before if before and not before.startswith("#") else paragraph(lines, i + 1, 1)
            explanation = re.sub(r"Table~\\ref\{[^}]*\}", "the table", explanation)
            out.append((f.name, "\n".join(lines[start : end + 1]), caption, explanation))
    return out


def main() -> None:
    parts = [START]
    for n, (name, table, caption, explanation) in enumerate(tables(), 1):
        parts += [
            "---",
            "class: paper-table" + (", wide" if max(len(row) for row in table.split("\n")) > 120 else ""),
            f"### From the paper: Table {n}",
            "",
            table,
            "",
            "???",
            f"Caption: {caption}",
            "",
            f"From the paper ({name}): {explanation}",
            "",
        ]
    parts.append(END)
    text = SLIDES.read_text(encoding="utf-8")
    block = "\n".join(parts)
    if START in text:
        text = text[: text.index(START)] + block + text[text.index(END) + len(END) :]
    else:
        text = text.rstrip("\n") + "\n\n" + block + "\n"
    SLIDES.write_text(text, encoding="utf-8")
    print(f"wrote {len(parts) and len(tables())} table slides into {SLIDES}")


if __name__ == "__main__":
    main()
