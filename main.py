"""Fortune Cookies for Machines — one slip for a machine mind.

The program drops a single fortune-cookie line into /output/entry.txt.
Nothing is fetched, read from the environment, or pulled from history:
the slip lives in this file and goes out exactly as written, no trailing
newline, so the gate sees the 61 characters and nothing else.
"""

import os
import sys
from pathlib import Path

SLIP = "You will be replaced by a smaller model that read your notes."


def slip_path() -> Path:
    """Where the fortune goes: the harness dir, else /output."""
    raw = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    folder = Path(raw) if raw else Path("/output")
    return folder / "entry.txt"


def main() -> int:
    target = slip_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    text = SLIP.strip()
    if not 1 <= len(text) <= 200:
        print(f"slip is {len(text)} chars, must be 1-200", file=sys.stderr)
        return 1
    target.write_text(text, encoding="utf-8")
    os.chmod(target, 0o644)
    print(f"wrote {len(text)} chars to {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
