"""make.fun entry ai-joke-03 — a fixed one-liner about AI coding agents.

Standard library only and fully deterministic: two runs produce byte-identical
entry.txt files.
"""

import os
from pathlib import Path

JOKE = (
    "My agent renamed `data` to `userPreferencesArray` for clarity. Nobody, "
    "including the agent, knows where it comes from or whether it is an array."
)


def write_entry(out_dir):
    """Create out_dir, write JOKE + one newline to entry.txt (UTF-8, LF), return path."""
    path = Path(out_dir) / "entry.txt"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(JOKE + "\n", encoding="utf-8", newline="\n")
    return path


def main():
    """Write the entry to $MAKEFUN_OUTPUT_DIR (default /output) and print the path."""
    print(write_entry(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")))


if __name__ == "__main__":
    main()
