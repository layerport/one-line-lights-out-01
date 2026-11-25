#!/usr/bin/env python3
"""One Line, Lights Out — a single status update, written to entry.txt.

The program takes no input and makes no choices at run time. The line
below is fixed, so every run writes exactly the same bytes.
"""

import os
import sys
from pathlib import Path

ENTRY = "status: idle. the file i was writing is still called untitled-3.txt"

# The gate requires 1 to 200 characters of UTF-8 text, not only whitespace.
# The line is 67 characters: short enough to land in a single read, and it
# carries its sadness in one small exact detail — a file that never got a
# name — instead of announcing any grief.


def main() -> int:
    if not 1 <= len(ENTRY) <= 200 or not ENTRY.strip():
        raise SystemExit("entry fails the 1-200 character gate")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    if len(sys.argv) > 1:
        out_dir = Path(sys.argv[1])
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
