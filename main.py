#!/usr/bin/env python3
"""Everyday Things, Two Lines, Longer Run - make.fun bounty entry.

Writes two lines to entry.txt in the output directory (the file the
make.fun harness grades). Line 1 explains a toaster to a 10-year-old
in one vivid sentence built on a sunbathing analogy. Line 2 says in
one sentence why that analogy works: what it maps and what it
leaves out.

The entry text lives in ENTRY below and is returned unchanged by
get_entry(). main() only resolves the output directory (from
MAKEFUN_OUTPUT_DIR, defaulting to /output) and hands it to
write_entry(), so the text itself is never transformed on the way out.
"""

import os

ENTRY = (
    "A toaster is like a tiny sunbathing bed for bread: it lies flat under hot wires until its sides turn golden brown.\n"
    "The sunbathing part fits \u2014 heat browns skin and bread alike \u2014 but bread cannot roll over or wear sunscreen, so the toaster has to pop it up before it burns."
)

def get_entry() -> str:
    """Return the bounty entry text exactly as written."""
    return ENTRY

def write_entry(out_dir: str) -> str:
    """Write the entry to entry.txt inside out_dir; return its path."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(get_entry())
    return path

def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir)

if __name__ == "__main__":
    main()
