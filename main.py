"""Write one short text to /output/entry.txt.

Deterministic: no randomness, no clock, no network. The same text is
written on every run, byte for byte.
"""

import os

SENTENCES = [
    "At the back of the library there is a door with no handle, only a "
    "small brass plate that reads 'return'.",
    "No one remembers what was borrowed, or who borrowed it.",
    "The librarian dusts the plate every morning, and waits.",
]

TEXT = " ".join(SENTENCES)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
