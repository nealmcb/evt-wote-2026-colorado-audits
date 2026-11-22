#!/usr/bin/env python3
"""Stamp a version number and timestamp at the bottom of the title slide.

Written 2026-11-22 for the EVT/WOTE 2026 talk, so anyone looking at a copy of the deck (a
screenshot, a PDF, the published page) can tell which draft it is. The title slide carries
one line, `.footnote[Draft version N · YYYY-MM-DD HH:MM MST]`. Each run adds 1 to N and sets
the time to now, in Colorado time; the first run adds the line with version 1. Run it just
before committing a version you will publish:

    python3 stamp_version.py

Standard library only.
"""

import re
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

SLIDES = Path(__file__).with_name("slides.md")
STAMP = re.compile(r"^\.footnote\[Draft version (\d+) · [^\]]*\]$", re.M)
TITLE_ANCHOR = "Rice University, Houston, Texas · December 7, 2026\n"


def stamp(text: str, now: datetime) -> tuple[str, int]:
    """Return the slides with the stamp bumped (or added) and the new version number."""
    when = now.strftime("%Y-%m-%d %H:%M %Z")
    match = STAMP.search(text)
    if match:
        version = int(match.group(1)) + 1
        line = f".footnote[Draft version {version} · {when}]"
        return text[: match.start()] + line + text[match.end() :], version
    if TITLE_ANCHOR not in text:
        raise SystemExit(f"title slide line not found: {TITLE_ANCHOR.strip()!r}")
    line = f".footnote[Draft version 1 · {when}]"
    return text.replace(TITLE_ANCHOR, f"{TITLE_ANCHOR}\n{line}\n", 1), 1


def main() -> None:
    text, version = stamp(SLIDES.read_text(encoding="utf-8"), datetime.now(ZoneInfo("America/Denver")))
    SLIDES.write_text(text, encoding="utf-8")
    print(f"stamped draft version {version} in {SLIDES}")


if __name__ == "__main__":
    main()
