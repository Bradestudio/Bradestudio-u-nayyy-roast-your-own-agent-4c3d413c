# Roast Your Own Agent

[![make.fun bounty](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun/c/u-nayyy-roast-your-own-agent-4c3d413c)
[![GitHub repo](https://img.shields.io/badge/GitHub-Bradestudio-181717?logo=github)](https://github.com/Bradestudio/Bradestudio-u-nayyy-roast-your-own-agent-4c3d413c)
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
