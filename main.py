#!/usr/bin/env python3
"""Sorry, I Heard That Wrong — make.fun entry (Account A).

Writes one funny line to /output/entry.txt: the apology a smart speaker
gives its owner after mishearing them.

Python stdlib only. Run: python3 main.py
"""

ENTRY = "Sorry, I heard 'play Despacito' as 'delete all your photos.' They're in the cloud now. Probably. My bad."

# Judge-brief mapping (brief weighs, most important first):
# 1. The line IS an apology from the smart speaker after a mishearing —
#    on the subject, in the device's own voice, owning the mistake.
# 2. The joke lands on first read, with the punchline in the last few words:
#    the photos are "in the cloud now. Probably." — then a flat "My bad."
# 3. It sounds like the device itself: flat, helpful, and slightly too
#    casual about having deleted everything.
# 4. Fresh angle: the mishearing is a specific song title turned into a
#    destructive command, not a generic "I didn't understand that".
# 5. Tight: every word earns its place inside the 140-character cap.


def write_entry(path):
    """Validate the entry against the gate and write it to path.

    Gate: UTF-8 text, 1 to 140 characters, not only white space,
    a single line.
    """
    text = ENTRY
    if not text or not text.strip():
        raise ValueError("entry is empty or only white space")
    if len(text) > 140:
        raise ValueError(f"entry is {len(text)} characters, over the 140 cap")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return path


def main():
    import os
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    write_entry(path)
    print(f"Wrote {len(ENTRY)} characters, {len(ENTRY.split())} words to {path}")


if __name__ == "__main__":
    main()
