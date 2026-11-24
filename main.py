#!/usr/bin/env python3
"""One Word for the Boss — make.fun entry.

The program writes exactly one word describing the boss to
/output/entry.txt: "Overlord".

Why this word: a boss who rules the office like a small kingdom —
every directive handed down from on high, every deadline a royal
decree, every meeting summoned at their pleasure. It is a single
word a colleague would actually use about the one they report to,
it lands on its own with no caption needed, it rings true for the
domineering boss everyone has met, it is not the first word anyone
reaches for, and it travels — a kitchen, a warehouse or an office
all have one.

Deterministic, standard library only, no network, no input.
"""

import os

WORD = "Overlord"

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Guard: the entry must be a single word within the 1-20 char gate.
    assert WORD.isalpha() and " " not in WORD, "entry must be a single word"
    assert 1 <= len(WORD) <= 20, "entry must be 1-20 characters"
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(WORD)
    print(WORD)


if __name__ == "__main__":
    main()
