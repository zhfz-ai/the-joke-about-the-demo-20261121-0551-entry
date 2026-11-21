#!/usr/bin/env python3
"""Entry for make.fun 'The joke about the demo'.

Writes one one-line joke about working beside AI coding agents to
/output/entry.txt (UTF-8, 1-280 code points), chmods it 0644, exits 0.
Standard library only; no network.
"""

import os
import sys

JOKE = (
    "The demo crashed on `import magic` — my agent had invented "
    "the library, written its README, and given it five stars."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    # Validate the joke against the gate before writing: UTF-8 text of
    # 1 to 280 Unicode code points, and not only white space.
    assert 1 <= len(JOKE) <= 280
    assert JOKE.strip()
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(JOKE)
    os.chmod(OUTPUT_PATH, 0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main())
