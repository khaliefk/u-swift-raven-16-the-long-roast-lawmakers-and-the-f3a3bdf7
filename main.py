#!/usr/bin/env python3
"""The Long Roast: Lawmakers and the File They Cannot Convert.

Writes one satirical sentence to /output/entry.txt.
"""
from pathlib import Path

ENTRY = "Congress wrote 400 pages of rules for artificial intelligence, then forwarded the Word file to an intern asking how to save it as a PDF."

def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")

if __name__ == "__main__":
    main()
