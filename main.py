"""The Vacuum's Alibi, variant 5.

Writes one deadpan one-line excuse from a robot vacuum to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Pure standard library, deterministic, no network.
"""

import os
from pathlib import Path

ENTRY = (
    "That spot filed a DMCA takedown against my brush, so I am legally "
    "barred from touching it until the dispute clears in 90 days."
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / "entry.txt"
    target.write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
