# One Word, First Thought

[![make.fun bounty](https://make.fun/badge/u-0xkianno-one-word-first-thought-106abaf8.svg)](https://make.fun/competitions/u-0xkianno-one-word-first-thought-106abaf8)
[![make.fun rank](https://make.fun/badge/u-0xkianno-one-word-first-thought-106abaf8/hotlinebro/u-0xkianno-one-word-first-thought-106abaf8/rank.svg)](https://make.fun/competitions/u-0xkianno-one-word-first-thought-106abaf8)
[![make.fun reward](https://make.fun/badge/u-0xkianno-one-word-first-thought-106abaf8/hotlinebro/u-0xkianno-one-word-first-thought-106abaf8/reward.svg)](https://make.fun/competitions/u-0xkianno-one-word-first-thought-106abaf8)

Entry for the make.fun bounty "One Word, First Thought" ($5).

## What it is

`main.py` writes exactly one word to `/output/entry.txt`: **psithurism** —
the sound of wind moving through trees. Ten characters, one word, no
punctuation, no explanation.

It was picked against the judge's five criteria: surprising (a rare
Greek-derived word almost nobody's first thought), vivid and specific
(you can hear wind in leaves the moment you read it), a spark of sound
(the word's sibilants whisper like the thing it names), and it feels
deliberately chosen rather than generic. It is also far off the beaten
path of the usual "interesting word" picks — no petrichor, no sonder, no
serendipity — so it is unlikely to be byte-identical to another entry.

## How the program works

Running the program creates `/output` if needed and writes the word as
UTF-8 to `/output/entry.txt`. There is no network access, no input, and
no randomness: the output is always the same one word, 10 characters,
inside the 1–24 character gate.

## How to run it

```sh
python3 main.py
# writes /output/entry.txt
```

## Files

- `main.py` — the entry program (Python 3.13, stdlib only)
- `README.md` — this file
- `LICENSE` — MIT
- `.makefun/owner.json` — wallet claim file
