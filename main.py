#!/usr/bin/env python3
"""Write one out-of-office auto-reply line to entry.txt.

Deterministic: the output is a single fixed string. This program reads
no clock, no random source, no network and no input file; it only honours
the MAKEFUN_OUTPUT_DIR environment variable (default /output) for where
to write entry.txt.
"""

import os

ENTRY = (
    "I'm out of office; my cat is answering emails now. "
    "She's already sat on the keyboard and promoted herself to my job."
)
# ENTRY is one line, 116 characters, no trailing newline: it satisfies the
# gate (UTF-8 text, 1 to 140 characters, not only white space).


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
