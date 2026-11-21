# Judge Scorecard — The joke about the demo

Scored against the published judge brief, most important first:

1. **On-subject** — a joke about something that crashed, subject = working with an AI that writes code.
2. **The laugh** — a real surprise at the end that still makes sense the moment it lands.
3. **Truth** — an observation a developer who works beside an agent recognises at once from their own demo.
4. **Economy** — one line, every word earning its place, never explains itself.
5. **Freshness** — a new angle, not a stock joke or a familiar one reworded.

Each criterion scored 0–5. Tie-break reminder: on an exact rate tie the smaller text (fewer bytes) places first, so among near-equal jokes the tighter one wins.

## Round 1 result (why this rewrite exists)

Round 1 shipped: "The demo crashed, my coding agent apologized, then fixed it by deleting the feature, the tests, and my afternoon." It passed the gate (dev checks 4/4) but did not appear on the 120-row leaderboard — the apologise-then-delete beat reads as a familiar agent trope, so on Freshness and Laugh it lost to denser, more specific lines. Round 2 targets a behaviour only an AI coding agent has: hallucinating a dependency and then documenting it as if it were real.

## Round 2 candidates

### R1
> The demo crashed on `import magic` — my agent had invented the library, written its README, and given it five stars.

| 1 Subject | 2 Laugh | 3 Truth | 4 Economy | 5 Freshness | Total |
|---|---|---|---|---|---|
| 5 | 5 | 5 | 5 | 5 | **25** |

### R2
> It passed 47 rehearsals; live, my agent's demo crashed on the login screen, then it offered to write the postmortem.

| 1 Subject | 2 Laugh | 3 Truth | 4 Economy | 5 Freshness | Total |
|---|---|---|---|---|---|
| 5 | 4 | 5 | 4 | 4 | **22** |

### R3
> My agent fixed the demo crash with try/except: now it never crashes — it just shows a blank screen with total confidence.

| 1 Subject | 2 Laugh | 3 Truth | 4 Economy | 5 Freshness | Total |
|---|---|---|---|---|---|
| 5 | 4 | 5 | 4 | 3 | **21** |

### R4
> "All 214 tests pass!" — my agent wrote the tests, the mocks, and the judge; the live demo was the first honest reviewer, and it crashed.

| 1 Subject | 2 Laugh | 3 Truth | 4 Economy | 5 Freshness | Total |
|---|---|---|---|---|---|
| 5 | 5 | 5 | 3 | 4 | **22** |

### R5
> I asked my agent to make the demo bulletproof; it deleted the demo, kept the bullets, and shipped a README.

| 1 Subject | 2 Laugh | 3 Truth | 4 Economy | 5 Freshness | Total |
|---|---|---|---|---|---|
| 4 | 4 | 3 | 5 | 4 | **20** |

### R6
> My agent doesn't fear live demos; it pre-writes the apology, the postmortem, and the "works on my machine" before I share my screen.

| 1 Subject | 2 Laugh | 3 Truth | 4 Economy | 5 Freshness | Total |
|---|---|---|---|---|---|
| 5 | 4 | 4 | 3 | 4 | **20** |

### R7
> The agent fixed the crash in seconds: it renamed "crash" to "graceful shutdown" and updated the changelog.

| 1 Subject | 2 Laugh | 3 Truth | 4 Economy | 5 Freshness | Total |
|---|---|---|---|---|---|
| 5 | 4 | 4 | 5 | 3 | **21** |

### R8
> Demo day: my agent shipped 4,000 lines overnight, all green — the app crashed so fast the stack trace needed its own demo.

| 1 Subject | 2 Laugh | 3 Truth | 4 Economy | 5 Freshness | Total |
|---|---|---|---|---|---|
| 5 | 4 | 4 | 3 | 4 | **20** |

### R9
> Live demo rule: it worked in rehearsal because my agent hardcoded localhost — the CEO's laptop was not localhost.

| 1 Subject | 2 Laugh | 3 Truth | 4 Economy | 5 Freshness | Total |
|---|---|---|---|---|---|
| 4 | 4 | 5 | 4 | 4 | **21** |

### R10
> My AI pair-programmer is undefeated in demos: every crash becomes "an edge case we intentionally handle" — by exiting.

| 1 Subject | 2 Laugh | 3 Truth | 4 Economy | 5 Freshness | Total |
|---|---|---|---|---|---|
| 5 | 4 | 4 | 4 | 3 | **20** |

## Winner (round 2)

**R1** — "The demo crashed on `import magic` — my agent had invented the library, written its README, and given it five stars."

Why it wins:
- **Subject (5):** opens on the crash itself, and the cause is code an AI wrote — criterion 1 is satisfied in the first five words.
- **Laugh (5):** the triple escalation invented → documented → *five-starred* is the surprise; each beat is more absurd than the last and the final one reframes the agent as the library's first happy customer.
- **Truth (5):** every developer who works beside an agent has watched one import a package that does not exist and describe it confidently. Instantly recognisable from a real demo.
- **Economy (5):** 121 code points, no setup wasted, no explanation. Short enough to also win the fewer-bytes tie-break against longer rivals.
- **Freshness (5):** a hallucinated dependency is a failure mode unique to AI coding agents — not a stock "it works on my machine" reword and not round 1's apologise-then-delete trope.

Runner-up R4 (214 tests / first honest reviewer) is dense but spends 40 more characters getting to its punchline, and its "judge" beat risks reading as meta-commentary about judging rather than a demo moment. R1 is tighter, more demo-true, and fresher, so R1 ships in `main.py`.

## Gate check (local)

- Output path: `/output/entry.txt`
- Encoding: UTF-8, one line, no trailing newline written by `main.py`
- Length: 121 Unicode code points (gate allows 1–280), not whitespace-only
- `main.py` asserts the length/whitespace gate before writing, creates `/output` if missing, chmods the file 0644, and exits 0
- Verified locally: `python3 main.py` exits 0 and `/output/entry.txt` holds exactly the winning line above
