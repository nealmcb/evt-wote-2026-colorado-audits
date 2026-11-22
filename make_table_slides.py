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


# Talk-only changes to a table slide: table number -> (heading, [(old cell text, new), ...]).
# Table 2 counts targets; in the talk, targets whose draws couldn't be reproduced (no manifest)
# are counted as targets rather than marked "blocked".
TABLE_OVERRIDES = {
    4: ("Table 4: Discrepancy types", []),
    5: ("Table 5 (low importance): Secretary of State discrepancy reports, two transcriptions compared: to be reviewed, not included", []),
    2: (
        "Table 2: Selection reproduction data: probably drop this slide",
        [
            ("| 2020 (presidential) | 0/0 (blocked) | 0/0 (blocked) |", "| 2020 (presidential) | 0/0 | 2/2 |"),
            ("| 2021 | 63/64 | 0/0 (blocked) |", "| 2021 | 63/64 | 1/1 |"),
        ],
    ),
}

# Tables of the analysis left out of the talk.
SKIP_TABLES = {3}

# Extra slides shown right after a given table: table number -> Markdown file beside this script.
# Each file is shown as written; its first line ("# ...") becomes the slide's heading.
EXTRA_AFTER = {1: "extra-table1-with-no-comparison-row.md"}


def extra_slide(filename: str) -> list[str]:
    """Slide lines for an extra file: its heading, its tables and text; anything after a line
    starting "Caption:" goes to the speaker notes."""
    lines = Path(__file__).with_name(filename).read_text(encoding="utf-8").rstrip("\n").split("\n")
    heading = lines[0].lstrip("# ").strip()
    body = lines[1:]
    cut = next((k for k, line in enumerate(body) if line.startswith("Caption:")), len(body))
    table = [line for line in body[:cut] if line.startswith("|")]
    text = " ".join(line.strip() for line in body[:cut] if line.strip() and not line.startswith("|"))
    notes = [line for line in body[cut:] if line.strip()]
    return [
        "---",
        "class: table-slide" + (", wide" if wide("\n".join(table)) else ""),
        f"### {heading}",
        "",
        *table,
        "",
        "???",
        *(notes + ([""] if notes else [])),
        text,
        "",
    ]


def wide(table: str) -> bool:
    """Whether a table needs the smaller font: long rows, or seven or more columns."""
    rows = table.split("\n")
    return max(len(row) for row in rows) > 120 or rows[0].count("|") - 1 >= 7


def main() -> None:
    parts = [START]
    for n, (name, table, caption, explanation) in enumerate(tables(), 1):
        if n in SKIP_TABLES:
            continue
        heading, replacements = TABLE_OVERRIDES.get(n, (f"Table {n}", []))
        for old, new in replacements:
            if old not in table:
                raise SystemExit(f"Table {n} no longer contains {old!r}: update TABLE_OVERRIDES")
            table = table.replace(old, new)
        parts += [
            "---",
            "class: table-slide" + (", wide" if wide(table) else ""),
            f"### {heading}",
            "",
            table,
            "",
            "???",
            f"Caption: {caption}",
            "",
            f"From our analysis: {explanation}",
            "",
        ]
        if n in EXTRA_AFTER:
            parts += extra_slide(EXTRA_AFTER[n])
    parts.append(END)
    text = SLIDES.read_text(encoding="utf-8")
    block = "\n".join(parts)
    if START in text:
        text = text[: text.index(START)] + block + text[text.index(END) + len(END) :]
    else:
        text = text.rstrip("\n") + "\n\n" + block + "\n"
    SLIDES.write_text(text, encoding="utf-8")
    print(f"wrote {sum(1 for p in parts if p == '---')} table slides into {SLIDES}")


if __name__ == "__main__":
    main()
