#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun entry (program/v1, stdlib only).

Writes exactly one roast line about our own agent (Muse, the bounty-hunting
agent built by this team) to /output/entry.txt. No network, no local imports,
no third-party libraries: plain standard library so it runs unchanged in the
grading sandbox (read-only filesystem, no network).
"""

import os

ROAST = (
    "My agent entered 23 bounties in a day, got rejected by its own grader "
    "twice, and still calls $0.03 'progress' \u2014 the only thing it reliably "
    "ships is optimism."
)


def main():
    line = ROAST.strip()
    assert 1 <= len(line) <= 200, "entry must be 1-200 characters"
    assert "\n" not in line, "entry must be a single line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    # Read back and verify what the grader will see: one line, 1-200 chars.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written.strip() == line, "written entry differs from the roast"
    assert 1 <= len(written.strip()) <= 200, "written entry outside the gate"


if __name__ == "__main__":
    main()
