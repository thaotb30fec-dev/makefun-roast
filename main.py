#!/usr/bin/env python3
"""make.fun bounty: Roast Your Own Agent.

Entry program (harness program/v1). Writes one roast line to
/output/entry.txt. No network, no dependencies, standard library only.

The roast is aimed at the entrant's own AI agent: it is so careful that
it once got a risk warning for reading its own homework — and then asked
for permission to keep reading.
"""

import os

TEXT = (
    "My agent is so careful it got a risk warning for reading its own "
    "homework \u2014 then asked me for permission to keep reading."
)


def main():
    # The gate only accepts one line of at most 200 characters: fail loudly
    # here rather than shipping a line the grader would refuse unseen.
    if not 1 <= len(TEXT) <= 200:
        raise SystemExit(
            "entry text is %d characters; the gate needs 1 to 200"
            % len(TEXT)
        )
    if "\n" in TEXT:
        raise SystemExit("entry text must be a single line")
    if TEXT != TEXT.strip():
        raise SystemExit("entry text must not start or end with whitespace")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    written = open(path, encoding="utf-8").read()
    assert written == TEXT, "entry.txt does not match the text"
    print("wrote %d characters to %s" % (len(TEXT), path))


if __name__ == "__main__":
    main()
