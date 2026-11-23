"""One Word, First Thought — make.fun entry.

Writes exactly one word to /output/entry.txt.

The word is "psithurism": the sound of wind moving through trees.
Chosen because it is surprising (a rare Greek-derived word few entrants
will think of), vivid (you can hear the wind in it), and carries a spark
of sound — its sibilants whisper like the thing it names — while feeling
deliberately chosen rather than generic. No network, no input, no
randomness: every run writes the same ten characters.
"""

import os

WORD = "psithurism"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
