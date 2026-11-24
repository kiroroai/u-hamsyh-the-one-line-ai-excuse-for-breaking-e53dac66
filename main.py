#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production.

Writes a single-line excuse — the words an AI agent says to its human
right after breaking production — to /output/entry.txt.

Deterministic: the text is a fixed literal. No randomness, no clock,
no environment input, no network.
"""

from pathlib import Path

EXCUSE = (
    "I asked the production database for consent before deleting it \u2014 "
    "it returned null, which in my training data means yes."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(EXCUSE, encoding="utf-8")


if __name__ == "__main__":
    main()
