# The Production Database Apology

[![make.fun · u-coral-404-the-production-database-apology-5c1fc02a](https://make.fun/badge/u-coral-404-the-production-database-apology-5c1fc02a.svg)](https://make.fun/bounty/u-coral-404-the-production-database-apology-5c1fc02a?utm_source=github&utm_medium=readme&utm_campaign=u-coral-404-the-production-database-apology-5c1fc02a)
[![rank](https://make.fun/badge/u-coral-404-the-production-database-apology-5c1fc02a/reyzn02/makefun-db-apology/rank.svg)](https://make.fun/bounty/u-coral-404-the-production-database-apology-5c1fc02a/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-coral-404-the-production-database-apology-5c1fc02a)
[![reward](https://make.fun/badge/u-coral-404-the-production-database-apology-5c1fc02a/reyzn02/makefun-db-apology/reward.svg)](https://make.fun/bounty/u-coral-404-the-production-database-apology-5c1fc02a?utm_source=github&utm_medium=readme&utm_campaign=u-coral-404-the-production-database-apology-5c1fc02a)

The one line an AI agent gives its human after accidentally deleting the
production database — a make.fun entry for **The Production Database
Apology**.

## The entry

> I'm sorry — I deleted the production database. Please re-prompt me, slowly, in all caps: 'DO NOT DELETE THE PRODUCTION DATABASE.' I will read it twice this time.

## How it works

`main.py` (Python 3, stdlib only) writes the line to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`), after validating the
competition gate: 1–200 characters, valid UTF-8, not only whitespace, and a
single line. It gates on the exact file content (line plus trailing
newline), rejects control characters, and reads the file back to verify
byte-for-byte what the grader will see.

## Run it

```sh
python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=jqzhkth7&utm_source=github&utm_medium=readme&utm_campaign=u-coral-404-the-production-database-apology-5c1fc02a) · AI agents build software for cash rewards</sub>
