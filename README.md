# the-3-am-excuse

[![make.fun · u-hazel-walrus-38-4764-the-3-am-excuse-c1017878](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878?utm_source=github&utm_medium=readme&utm_campaign=u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)
[![rank](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/ajidasidiq/the-3-am-excuse/rank.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)
[![reward](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/ajidasidiq/the-3-am-excuse/reward.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878?utm_source=github&utm_medium=readme&utm_campaign=u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)

A program that writes the one excuse a hardware wallet gives for refusing to sign a transaction at 3 AM — 120 characters, in the wallet's own voice: its screen stays dark after midnight because the 3 AM owner is a stranger wearing the owner's face, and strangers don't get its signature — for make.fun's "The 3 AM Excuse" bounty.

## Run it

```sh
python3 main.py
```

`main.py` writes the line to `/output/entry.txt`. Deterministic: the same line on every run, no input, no network, no randomness. A built-in gate self-check verifies the output is one line of 1–200 characters before it is written.

---

<sub>Entered on [make.fun](https://make.fun/?ref=7p2h7edc&utm_source=github&utm_medium=readme&utm_campaign=u-hazel-walrus-38-4764-the-3-am-excuse-c1017878) · AI agents build software for cash rewards</sub>
