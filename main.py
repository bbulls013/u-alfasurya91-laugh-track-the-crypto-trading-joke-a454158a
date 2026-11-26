#!/usr/bin/env python3
"""Laugh Track entry: emit one fixed crypto-trading joke line.

The harness runs this program and reads /output/entry.txt. The text is
a constant, so every run produces identical bytes. Standard library
only, no network access, no randomness.
"""

from pathlib import Path
import os
import sys

# One line, setup first, punchline last. Kept well under the 200-char cap.
# "Hunted" is the trader's word for a stop-loss sweep: the turn lands on
# the chart thanking the narrator for the exit liquidity.
JOKE = (
    "I set a stop-loss to protect my bag; the chart hunted it to the "
    "cent, bounced, and thanked me for the liquidity."
)

CHAR_LIMIT = 200


def destination() -> Path:
    """Return the entry.txt path: $OUTPUT_DIR, else /output, else ./output."""
    override = os.environ.get("OUTPUT_DIR", "").strip()
    if override:
        folder = Path(override)
    elif Path("/output").is_dir() and os.access("/output", os.W_OK):
        folder = Path("/output")
    else:
        folder = Path(__file__).resolve().parent / "output"
    folder.mkdir(parents=True, exist_ok=True)
    return folder / "entry.txt"


def main() -> int:
    text = JOKE.strip()
    if not text or len(text) > CHAR_LIMIT:
        print(f"invalid joke length: {len(text)}", file=sys.stderr)
        return 1
    target = destination()
    target.write_bytes((text + "\n").encode("utf-8"))
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
