#!/usr/bin/env python3
"""Loading screen tip for a stressed developer and their AI coding agent.

The joke lands because it is about both of them at once: the agent has
just burned a whole round-trip rewriting a function and then quietly
reverting it, and the developer — who watched the diff appear, vanish,
and reappear — knows exactly whose version was better. Neither side will
say so out loud. The agent cannot admit it wasted the turn; the developer
cannot admit the machine had the better idea. So they sit there together,
mid-build, in a standoff of pure professional pride, while the loading
spinner does the only honest work in the room.

That is why it is the whole entry: one line, 129 characters, written to
/output/entry.txt.
"""

from pathlib import Path

TIP = (
    "Tip: your agent rewrote that function, then rewrote it back. "
    "You both know whose version was right. "
    "Neither of you will admit it."
)


def main() -> None:
    path = Path("/output/entry.txt")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(TIP + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
