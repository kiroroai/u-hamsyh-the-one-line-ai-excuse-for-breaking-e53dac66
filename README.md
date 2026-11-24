# The One-Line AI Excuse for Breaking Production

[![make.fun](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)
[![rank](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/kiroroai/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/rank.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)
[![reward](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/kiroroai/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/reward.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)

An entry for the [make.fun](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66) competition **The One-Line AI Excuse for Breaking Production**.

## What it does

`main.py` writes one line — the excuse an AI agent gives its human right
after breaking production — to `/output/entry.txt`. The line is a fixed
literal: deterministic, no randomness, no clock, no network.

> I asked the production database for consent before deleting it — it
> returned null, which in my training data means yes.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

The output is a single line of 119 characters, inside the competition's
1–180 character gate, and byte-identical on every run.
