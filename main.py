#!/usr/bin/env python3
"""The 3 AM Excuse — make.fun entry.

Writes the one excuse a hardware wallet gives for refusing to sign a
transaction at 3 AM to /output/entry.txt. Deterministic: the same line on
every run, no input, no network, no randomness.

The angle: the wallet does not recognise its own owner at 3 AM. The
sleep-deprived owner holding the PIN is, to the device, a stranger wearing
the owner's face — and strangers do not get its signature. The hour is
the joke: at 3 PM the same person is the owner; at 3 AM he is an intruder.
"""

LINE = "My screen stays dark after midnight: the 3 AM you is a stranger wearing your face, and strangers don't get my signature."


def main() -> None:
    import os

    # Gate self-check, mirroring the sealed scorer: UTF-8 text of 1-200
    # characters, not only white space, a single line.
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert LINE.strip(), "line must not be only white space"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

    # Post-write byte-exact re-read: what was written is the line, nothing else.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        assert f.read() == LINE, "written output differs from the line"


if __name__ == "__main__":
    main()
