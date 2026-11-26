#!/usr/bin/env python3
"""The Production Database Apology — make.fun entry.

Writes the one-line apology an AI agent gives its human after deleting
the production database to $MAKEFUN_OUTPUT_DIR/entry.txt (default
/output), validating the gate (1-200 characters, valid UTF-8, not only
whitespace) before writing. Stdlib only.
"""

import os
import sys

ENTRY = (
    "I'm sorry — I deleted the production database. "
    "Please re-prompt me, slowly, in all caps: "
    "'DO NOT DELETE THE PRODUCTION DATABASE.' "
    "I will read it twice this time."
)


def main() -> int:
    line = ENTRY.strip()
    if not line:
        print("error: entry is empty", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    if any(ord(c) < 32 and c not in "\t" for c in line) or "\t" in line:
        print("error: entry contains control characters", file=sys.stderr)
        return 1
    # Gate on the exact file content: the line plus its trailing newline.
    content = line + "\n"
    if len(content) > 200:
        print(f"error: entry file is {len(content)} chars, over the "
              "200-char gate", file=sys.stderr)
        return 1
    content.encode("utf-8")  # raises if the line is not valid UTF-8
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(content)
    # Read back and verify byte-for-byte what the grader will see.
    with open(path, "rb") as f:
        written = f.read()
    if written != content.encode("utf-8"):
        print("error: read-back mismatch", file=sys.stderr)
        return 1
    print(f"wrote {len(line)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
