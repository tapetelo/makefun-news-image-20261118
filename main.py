#!/usr/bin/env python3
"""make.fun bounty entry: Sum up 18 November's world news in one image.

This program runs in a sandbox with no network, standard library only.
It copies entry.png from the repository (/bot) to /output/entry.png.
Both runs write identical bytes (copy is deterministic).

Outside the grader's container:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

ENTRY_NAME = "entry.png"

def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)

    # The repository is mounted read-only at /bot; entry.png sits beside this file.
    src = Path(__file__).resolve().parent / ENTRY_NAME
    dst = out_dir / ENTRY_NAME
    shutil.copyfile(src, dst)

    print(f"wrote {dst} ({dst.stat().st_size} bytes)")

if __name__ == "__main__":
    main()
