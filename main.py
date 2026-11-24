#!/usr/bin/env python3
"""Everyday Things, Two Lines, Longer Run - make.fun bounty entry.

Writes two lines to /output/entry.txt (the file the make.fun harness
grades). Line 1 explains a toaster to a 10-year-old in one vivid
sentence built on a sunbathing analogy. Line 2 says in one sentence
why that analogy works: what it maps and what it leaves out.
"""

import os

ENTRY = (
    "A toaster is like a tiny sunbathing bed for bread: it lies flat under hot wires until its sides turn golden brown.\n"
    "The sunbathing part fits \u2014 heat browns skin and bread alike \u2014 but bread cannot roll over or wear sunscreen, so the toaster has to pop it up before it burns."
)

def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
