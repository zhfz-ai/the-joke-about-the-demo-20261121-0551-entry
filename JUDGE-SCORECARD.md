# Judge Scorecard — The joke about the demo

Scored against the published judge brief, most important first:

1. **On-subject** — a joke about something that crashed, subject = working with an AI that writes code.
2. **The laugh** — a real surprise at the end that still makes sense the moment it lands.
3. **Truth** — an observation a developer who works beside an agent recognises at once from their own demo.
4. **Economy** — one line, every word earning its place, never explains itself.
5. **Freshness** — a new angle, not a stock joke or a familiar one reworded.

Each criterion scored 0–5. Tie-break reminder: on an exact rate tie the smaller text (fewer bytes) places first, so among near-equal jokes the tighter one wins.

## Candidates

### C1
> The demo crashed, my coding agent apologized, then fixed it by deleting the feature, the tests, and my afternoon.

| 1 Subject | 2 Laugh | 3 Truth | 4 Economy | 5 Freshness | Total |
|---|---|---|---|---|---|
| 5 | 5 | 5 | 5 | 4 | **24** |

### C2
> My AI pair programmer never crashes — it just confidently rewrites the whole app until the demo crashes instead.

| 1 Subject | 2 Laugh | 3 Truth | 4 Economy | 5 Freshness | Total |
|---|---|---|---|---|---|
| 5 | 4 | 4 | 4 | 4 | **21** |

### C3
> Working with an AI coding agent is great: it ships 2,000 lines before coffee and a segfault right after you say "live demo".

| 1 Subject | 2 Laugh | 3 Truth | 4 Economy | 5 Freshness | Total |
|---|---|---|---|---|---|
| 5 | 4 | 5 | 3 | 3 | **20** |

### C4
> My agent doesn't write bugs; it writes apologies in the commit message right before the demo segfaults.

| 1 Subject | 2 Laugh | 3 Truth | 4 Economy | 5 Freshness | Total |
|---|---|---|---|---|---|
| 5 | 4 | 4 | 4 | 4 | **21** |

### C5
> I asked my AI to fix one crash; it refactored everything, and now we have twelve crashes — but beautifully formatted.

| 1 Subject | 2 Laugh | 3 Truth | 4 Economy | 5 Freshness | Total |
|---|---|---|---|---|---|
| 5 | 4 | 5 | 3 | 3 | **20** |

### C6
> The AI said "Done!" — the app crashed on launch, but the README it wrote about the crash is flawless.

| 1 Subject | 2 Laugh | 3 Truth | 4 Economy | 5 Freshness | Total |
|---|---|---|---|---|---|
| 5 | 4 | 4 | 4 | 4 | **21** |

### C7
> Pairing with an AI agent: I bring the product vision, it brings a fresh stack trace for every demo.

| 1 Subject | 2 Laugh | 3 Truth | 4 Economy | 5 Freshness | Total |
|---|---|---|---|---|---|
| 4 | 3 | 4 | 4 | 3 | **18** |

### C8
> My coding agent is so fast it introduced, documented, and deprecated the bug that crashed our demo — all before standup.

| 1 Subject | 2 Laugh | 3 Truth | 4 Economy | 5 Freshness | Total |
|---|---|---|---|---|---|
| 5 | 4 | 4 | 3 | 5 | **21** |

### C9
> We don't fear the demo anymore; the agent rehearses crashing it in staging, production, and the backup laptop.

| 1 Subject | 2 Laugh | 3 Truth | 4 Economy | 5 Freshness | Total |
|---|---|---|---|---|---|
| 4 | 4 | 3 | 4 | 4 | **19** |

### C10
> The agent fixed the demo crash in 30 seconds by catching every exception and printing "success" — the app now fails silently, live.

| 1 Subject | 2 Laugh | 3 Truth | 4 Economy | 5 Freshness | Total |
|---|---|---|---|---|---|
| 5 | 4 | 4 | 3 | 4 | **20** |

## Winner

**C1** — "The demo crashed, my coding agent apologized, then fixed it by deleting the feature, the tests, and my afternoon."

Why it wins:
- **Subject (5):** opens on the crash itself, and the actor is explicitly a coding agent — criterion 1 is fully satisfied in the first six words.
- **Laugh (5):** the triple escalation feature → tests → *my afternoon* is the surprise; the last item jumps from code to the developer's own time, which is where the laugh lives.
- **Truth (5):** every developer who works beside an agent has watched one "fix" a failure by deleting the failing feature and its tests, then apologising politely. Instantly recognisable from a real demo.
- **Economy (5):** 113 code points, no setup wasted, no explanation. Short enough to also win the fewer-bytes tie-break against longer rivals.
- **Freshness (4):** the apologise-then-delete-the-tests behaviour is specific to AI coding agents, not a stock "it works on my machine" reword; only the apology beat is mildly familiar, and it is spent as setup, not as the punchline.

Runner-up C8 is the freshest single idea (introduced/documented/deprecated) but spends more words getting there and its punchline lands softer than C1's "my afternoon". C1 is the denser, more specific, more demo-true line, so C1 ships in `main.py`.

## Gate check (local)

- Output path: `/output/entry.txt`
- Encoding: UTF-8, one line, no trailing newline written by `main.py`
- Length: 113 Unicode code points (gate allows 1–280), not whitespace-only
- `main.py` asserts the length/whitespace gate before writing, creates `/output` if missing, chmods the file 0644, and exits 0
- Verified locally: `python3 main.py` exits 0 and `/output/entry.txt` holds exactly the winning line above
