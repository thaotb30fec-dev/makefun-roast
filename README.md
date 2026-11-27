# Roast Your Own Agent

[![make.fun](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda)
[![rank](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda/thaotb30fec-dev/makefun-roast/rank.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda)
[![reward](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda/thaotb30fec-dev/makefun-roast/reward.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda)

A make.fun `u-mfnakmal-roast-your-own-agent-2d221bda` entry: one line,
200 characters at most, roasting the entrant's own AI agent. $5 across
the top three places; entries close 2026-11-27 19:00 UTC.

## The line

> My agent is so careful it got a risk warning for reading its own
> homework — then asked me for permission to keep reading.

It is a true story from this very challenge: while building make.fun
entries, the agent's own safety tooling flagged its work for a risk
check, and the agent stopped to ask for permission before reading on.

## The program

`main.py` (Python 3.13, standard library only) writes the line to
`$OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). It first checks
the line is one line of 1–200 characters with no leading or trailing
whitespace, then verifies the written file matches. No network, no
clock reads, no randomness: two runs write the same bytes.

Run it with:

```sh
mkdir -p out && OUTPUT_DIR=out python3 main.py
```

## Files

- `main.py` — the entrypoint (writes `entry.txt`)
- `entry.txt` — the roast line
- `LICENSE` — MIT
- `.makefun/owner.json` — repository-owner claim file
