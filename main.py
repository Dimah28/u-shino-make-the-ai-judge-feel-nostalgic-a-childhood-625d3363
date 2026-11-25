#!/usr/bin/env python3
"""Make the AI Judge Feel Nostalgic: A Childhood Memory.

Writes one single sentence (277 characters) to entry.txt: a summer
evening in grandmother's kitchen, the smell of fresh rice, the burnt
crust saved just for me, her hum — and the silent kitchen now, still
listening for it. Pure Python 3.13 standard library, no network,
fully deterministic: the same text on every run.

Why this line (judge brief + winning-pattern study):
- concrete place, time and sensation: grandmother's kitchen, summer
  evening, steaming rice, the crisp burnt crust, a hum;
- small honest detail, not greeting-card sentiment: the crust at the
  bottom of the pot, saved just for one child;
- one clean sentence, every word earning its place;
- twist at the end: the kitchen is silent now, the hum stopped years
  ago — the warm ache that lingers after the sentence ends.
"""

import os
import sys

TEXT = (
    "Every summer evening my grandmother ladled rice still steaming "
    "from the pot, saved the crisp burnt crust at the bottom just for "
    "me, and hummed a song her own mother sang, and now when my rice "
    "cooker clicks I stand in a silent kitchen listening for a hum "
    "that stopped years ago."
)

# Competition rule: the text must be one sentence of 1 to 280
# characters, counted as Unicode code points, not only whitespace.
# One period only, at the very end: a single clean sentence.
assert 1 <= len(TEXT) <= 280, f"ENTRY length {len(TEXT)} outside 1-280"
assert TEXT.count(".") == 1 and TEXT.endswith("."), "ENTRY must be one sentence"


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get(
        "OUTPUT_PATH", "/output"
    )
    if out_dir.endswith("entry.txt"):
        out_dir = os.path.dirname(out_dir)
    if not (1 <= len(TEXT) <= 280):
        print(f"entry must be 1-280 characters, got {len(TEXT)}", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
