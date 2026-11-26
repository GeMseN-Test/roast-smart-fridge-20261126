#!/usr/bin/env python3
"""Roast the Smart Fridge: One Line, Best Laugh Wins.

The entry is a single roast line, spoken by the smart fridge itself.
The program writes that one line to /output/entry.txt for the judge.
"""

import os

LINE = "My screen shows ads for cheese you own while the ice maker rattles like a slot machine — I am a billboard that keeps milk cold."
# One line, 127 characters (limit 160), spoken in the first person by the fridge.


def main():
    os.makedirs("/output", exist_ok=True)
    # Write exactly the line, no trailing newline: the scorer counts 1-160 chars.
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
