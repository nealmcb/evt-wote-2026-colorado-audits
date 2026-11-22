class: center, middle

## Evidence and Best Practices from Colorado Audits

### Over 7,000 contests in a decade

Neal McBurnett, Lori Stevens, John Caron, Mike Raisch

EVT/WOTE 2026

???
15 minutes in all: about 11 of talk, 4 for questions.

To display locally, run `view-presentation`.
To make a PDF: `decktape http://localhost:8000/#1 evt-wote-2026.pdf`

---
## Why this matters now

* Risk-limiting audits are under attack from skeptics
* Officials trusting the audit is not enough
* The public needs to be able to check it for itself

**Goal:** move Colorado from *officials trust the audit*
to *anyone can verify it*

---
## How Colorado audits

* Every ballot is scanned; the **cast vote record (CVR)** records every vote
* A public dice roll seeds the random sample
* Audit boards read each sampled ballot card and compare it with its CVR row

So **every contest on a sampled card** is compared,
not just the targeted ones

???
Targeted contests drive the sample size; the rest are compared "opportunistically".
An audit of a contest is not the same as a risk-limiting audit of it.

---
## A decade of ballot-level evidence

<img src="contests.svg" width="100%">

Over **7,000 contests** since 2019, about **475 targeted**

???
6,520 contests from 2019 to the 2026 primary (2020 presidential's 2 omitted), plus about 1,000 in this week's 2026 general.
Source: the paper's Table 1, from its rebuilt cross-election database (to be published).

---
## What the data show

* **965,254** contest comparisons; **637** discrepancies (0.066%)
* Rates vary about twentyfold between elections
* Ten years: four contests needed a 3rd round, one a 4th
* Causes: audit boards' data-entry slips, occasional wrong ballots
  (voters' overvotes, entered as marked, are not discrepancies)

**But:** the evidence was scattered and short-lived;
we had to mirror and rebuild it

???
Discrepancies: o2/o1 overstatements and u1/u2 understatements, Kaplan-Markov typing matching CORLA's rule.
Mirror: github.com/nealmcb/auditcenter, files kept since 2017 at the Audit Center's own paths.

---
## The 2026 pilots: verifiable observation

* All evidence **committed before the dice roll**:
  signed (Sigstore), timestamped (OpenTimestamps), published
* **Redacted CVRs** from La Plata, Morgan and Weld
* Observers checked each ballot read aloud against the CVR
* Targeted and style-based extra draws

???
Thanks to the clerks: Tiffany Lee (La Plata), Carly Koppes (Weld), Kevin Strauch (Morgan).

---
## What observers found

* 71 targeted contests: 69 met the risk limit in round 1, 2 in round 2
* In Weld, the redacted CVR matched CORLA's own CVR
  on every audited card: **5,980 of 5,980** choices
* Observers' records: signed on their own devices,
  checkable without trusting our software

???
The Weld check uses CORLA's published round comparison file.
Write-up: docs/CLI_OBSERVER_SI.md in github.com/nealmcb/corla-observer

---
## Best practices and what's next

* **Commit** the audit's inputs publicly before the seed
* **Redact automatically** (anonymize_cvr) and publish no small counts
* **Style-based RLAs**: cover more contests with less work
* **Independent observers** with verifiable records

???
anonymize_cvr 0.4.0: precinct redaction by default, rare contests and rare ballot types redacted.

---
class: center, middle

## Thanks

Matt Crane (CCCA), the clerks of La Plata, Morgan and Weld,
and the Colorado Secretary of State's office

github.com/nealmcb/corla-observer
github.com/nealmcb/anonymize_cvr
github.com/nealmcb/auditcenter

sites.google.com/view/auditenhancement
