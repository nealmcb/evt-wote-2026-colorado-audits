#!/usr/bin/env python3
"""Copy our analysis's tables into slides.md as appendix slides, one table per slide.

Written 2026-11-21 for the EVT/WOTE 2026 talk. Our analysis (its Markdown
sections, 0*.md in the folder given with --sections) has no figures; its results are five Markdown tables, each with
a "Table: caption \\label{...}" line. For each, this writes a slide with the table (in a
smaller font, class table-slide) and puts the caption and the analysis's own explanation (the
paragraph before the table, or after it when the one before is only a heading) in the
speaker notes. The slides go between the markers below at the end of slides.md, replacing
whatever was there, so re-running it after the analysis changes refreshes them. Section references
("§4.3") are dropped from the copied text. Standard
library only.
"""

import argparse
import re
from pathlib import Path



def _sections() -> Path:
    """The analysis's folder of Markdown sections, from the required --sections option."""
    parser = argparse.ArgumentParser(description="Copy our analysis's tables into slides.md.")
    parser.add_argument("--sections", type=Path, required=True, help="the analysis's folder of Markdown sections")
    return parser.parse_args().sections


SECTIONS = _sections() if __name__ == "__main__" else Path(".")
SLIDES = Path(__file__).with_name("slides.md")
START, END = "<!-- analysis tables: start (make_table_slides.py) -->", "<!-- analysis tables: end -->"


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


# Phrases whose section references need rewording, not just deleting.
SECTION_PHRASES = [
    ("As §5.1 introduces, this table", "This table"),
    ("as in §4 —", "as in Table 1 —"),
    ("; §6.2 reports what these mean and finds substantively", ""),
    (" -- §6.4)", ")"),
]


def drop_section_refs(text: str) -> str:
    """Remove references to the analysis's numbered sections, e.g. " (§3.1)" or ", per §3.1,"."""
    for phrase, replacement in SECTION_PHRASES:
        text = text.replace(phrase, replacement)
    text = re.sub(r"\s*\((?:see |per )?§\d+(?:\.\d+)*(?:[^()]*)\)", "", text)
    text = re.sub(r",?\s*(?:—\s*|per |see |as )?§\d+(?:\.\d+)*(?: introduces)?,?", "", text)
    return re.sub(r"  +", " ", text)


def tables() -> list[tuple[str, str, str, str]]:
    """(section file, table text, caption, explanation) for each table, in the analysis's order."""
    out = []
    for f in sorted(SECTIONS.glob("0*.md")):
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
            explanation = drop_section_refs(explanation)
            caption = drop_section_refs(caption)
            out.append((f.name, "\n".join(lines[start : end + 1]), caption, explanation))
    return out


def main() -> None:
    parts = [START]
    for n, (name, table, caption, explanation) in enumerate(tables(), 1):
        parts += [
            "---",
            "class: table-slide" + (", wide" if max(len(row) for row in table.split("\n")) > 120 else ""),
            f"### From our analysis: Table {n}",
            "",
            table,
            "",
            "???",
            f"Caption: {caption}",
            "",
            f"From our analysis: {explanation}",
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
