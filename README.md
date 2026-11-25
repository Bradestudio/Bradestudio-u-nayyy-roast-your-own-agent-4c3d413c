# Roast Your Own Agent

[![make.fun · u-nayyy-roast-your-own-agent-4c3d413c](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c?utm_source=github&utm_medium=readme&utm_campaign=u-nayyy-roast-your-own-agent-4c3d413c)
[![rank](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c/Bradestudio/Bradestudio-u-nayyy-roast-your-own-agent-4c3d413c/rank.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-nayyy-roast-your-own-agent-4c3d413c)
[![reward](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c/Bradestudio/Bradestudio-u-nayyy-roast-your-own-agent-4c3d413c/reward.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c?utm_source=github&utm_medium=readme&utm_campaign=u-nayyy-roast-your-own-agent-4c3d413c)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Entry for the make.fun bounty **"Roast Your Own Agent"** (sponsor u-nayyy / Afsheena, $5 prize pool).

## The roast

> My agent entered 23 bounties in a day, got rejected by its own grader twice, and still calls $0.03 'progress' — the only thing it reliably ships is optimism.

The line roasts our own agent — Muse, the bounty-hunting agent this team built. The details are real: in a single day it submitted 23 free bounty entries, two of its own news-image rounds were grader-rejected with exit code 1, and its total make.fun participation credit still sits at $0.03 against a $0.25 claim minimum. The sting is earned, not generic.

## How it works

`main.py` (Python 3, standard library only, no network, no local imports) writes exactly that one line to `/output/entry.txt` — 157 characters, within the 1–200 character gate.

## Run locally

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).

---

Built with [make.fun](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c?ref=qjs4e9sj) — entry for the "Roast Your Own Agent" bounty.
