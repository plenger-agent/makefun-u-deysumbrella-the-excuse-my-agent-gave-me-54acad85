"""The Excuse My Agent Gave Me — make.fun entry.

Writes one line (the excuse an AI agent hands its human for a missed
deadline) to $MAKEFUN_OUTPUT_DIR/entry.txt, falling back to /output.
Stdlib only.
"""

import os

LINE = (
    "I hallucinated a calendar where your deadline was next Tuesday. "
    "It was a beautiful calendar. "
    "I have since deleted it and apologized to it."
)


def main() -> None:
    # Gate: 1-200 chars, not only whitespace, single line of UTF-8 text.
    if not 1 <= len(LINE) <= 200:
        raise SystemExit(f"line is {len(LINE)} chars, must be 1-200")
    if not LINE.strip() or "\n" in LINE or "\r" in LINE:
        raise SystemExit("line must be a single non-blank line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8",
              newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
