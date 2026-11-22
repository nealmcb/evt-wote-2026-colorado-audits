class: center, middle

## Draft: do not trust any of this yet

Nearly unreviewed. Drafted with Claude, which repeatedly restated
points it had misunderstood.

The numbers rest on complicated notions: CORLA targeting
**county portions** of multi-county contests on one county's margin,
the risk levels of **opportunistic** contests, and
**missing or inconsistent data** in the state's exports.

Check every figure against our analysis and data. See README.md.

???
Remove this slide once the talk has been reviewed.

---
class: center, middle

## Evidence and Best Practices from Colorado Audits

### 7,503 contests in a decade

Neal McBurnett, Lori Stevens, John Caron, Mike Raisch

[EVT/WOTE 2026](https://centerforvoting.rice.edu/electronic-voting-technologies-workshop-trustworthy-elections-conference)

Rice University, Houston, Texas · December 7, 2026

???
15 minutes in all: about 11 of talk, 4 for questions.

To display locally, run `view-presentation`.
To make a PDF: `decktape http://localhost:8000/#1 evt-wote-2026.pdf`
To publish, run: rsync -av --exclude '.git' --exclude 'neal-ignore' ../evt-wote-2026-colorado-audits "$DIR"/site/elections/ and deploy that site (its PLAN.md: generate_directory_manifest.py, then npx wrangler deploy)
To visit: google-chrome [https://neal.mcburnett.org/elections/evt-wote-2026-colorado-audits/](https://neal.mcburnett.org/elections/evt-wote-2026-colorado-audits/)

---
## Why this matters now

* Risk-limiting audits are under attack from skeptics
* Officials trusting the audit is not enough
* The public needs to be able to check it for itself

**Goal:** move Colorado from *officials trust the audit*
to *anyone can verify it*

---
## How Colorado audits

* Every ballot is scanned centrally; the **cast vote record (CVR)** records every vote
* A public dice roll seeds a publicly verifiable random sample
* Audit boards review each sampled voter-verified ballot card and report every mark on every contest, without knowing how the system reported it
* The CORLA software compares the two interpretations, driving the targeted contests (only) to meet the risk limit, by expanding the selection in extra rounds as necessary

* The other contests are all audited *opportunistically*, but not guaranteed to meet a risk limit

Note: some data is still incomplete, these figures will be updated as we fill in the gaps

???
Targeted contests drive the sample size; the rest are compared "opportunistically".
An audit of a contest is not the same as a risk-limiting audit of it.

---
## A decade of ballot-level evidence

<img src="contests.svg" width="100%">

**7,503 contests** since 2019:
**529 targeted**, **6,974 opportunistic**

???
7,503 contests from 2019 through the 2026 general, as in Table 1 of our analysis; 981 of them in the 2026 general. The chart leaves out the 2020 presidential primary's 2 contests (7,501 shown, 527 targeted).
Targeted: the whole contest was a formal sampling target. A county portion of a multi-county contest, targeted on one county's margin, does not make the contest targeted.
Opportunistic: every other contest, audited on the cards drawn for the targets. Each gets an opportunistic risk level, which CORLA does not report.
Source: Table 1 of our analysis, from the rebuilt cross-election database, which we may publish.

---
## What the data show

* **1,448,499** contest comparisons; **959** discrepancies (0.066%)
* Rates vary about twentyfold between elections
* Ten years: five contests went to round 3, one to round 4
* Causes: mostly audit boards' ballot retrieval or data-entry slips, occasional adjudication or vote interpretation differences

???
Discrepancies: o2/o1 overstatements and u1/u2 understatements, Kaplan-Markov typing matching CORLA's rule.
Mirror: [github.com/nealmcb/auditcenter](https://github.com/nealmcb/auditcenter), files kept since 2017 at the Audit Center's own paths.
Rounds: a target is what CORLA sizes a sample for, either a whole contest or a county portion of a multi-county contest sized on one county's margin. The five targets that reached round 3 were all whole contests: Otero County Clerk (2018 general, round 4), Proposition DD (2019, statewide), City of Colorado Springs Ballot Question 2C (2020 general), Kiowa County Treasurer (2022 general), Dove Creek Ambulance District Ballot Issue 6A (2024 general). Source: the Audit Center's round files, as mirrored at github.com/nealmcb/auditcenter.

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

* 52 targeted contests: 50 met the risk limit in round 1, 2 in round 2
* In Weld, the redacted CVR matched CORLA's own CVR
  on every audited card: **5,980 of 5,980** choices
* Observers' records: uploaded live, but signed on their own devices,
  checkable without trusting our server software (*a model for CORLA itself?*)

???
Targeted contests from CORLA's round 2 contest.csv and results report; round 2 was Jackson County Assessor and Montezuma County Commissioner District 1. CORLA's 71 targets are these 52 targeted contests plus 19 county portions of multi-county contests, each sized on one county's margin; a county portion is a target but not a targeted contest, so the 19 are not counted here.
The Weld check uses CORLA's published round comparison file.
Write-up: [docs/CLI_OBSERVER_SI.md](https://github.com/nealmcb/corla-observer/blob/main/docs/CLI_OBSERVER_SI.md) in [github.com/nealmcb/corla-observer](https://github.com/nealmcb/corla-observer)

---
class: table-slide
## Style-based audits of legislative contests (draft for John to check)

| Colorado general election | 2022 | 2024 | 2026 |
|---|---:|---:|---:|
| Contested House and Senate contests | 76 | 75 | 74 |
| Targeted | 1 | 1 | 4 |
| Risk level at or below 3% | 36 | 18 | 32 |
| Cards examined, all contests | 6,454 | 4,897 | 5,553 |
| Est. cards for all at 3%, style-based | ≤ 6,400 | ≤ 5,200\* | ≤ 3,900 |

* Diluted margin over the contest's own cards: 2024 House District 1
  (10,071 votes), 0.68% → 26.4%, so ~1,064 → ~26 cards
* rlauxe's 2024 simulation: targets, statewide and most legislative contests in 4,792 cards
* Needs card styles in the ballot manifest

\*Not counting two House contests in recount range

???
Draft for John Caron to check, revise or reject. Every number below is from 2024, 2022 or 2026 general-election data as stated; estimates are labelled.

Counts and risk levels: our analysis's cross-election database, which we may publish (true_contests, risk_calculations at each contest's latest round, ballot_comparisons). "Contested" leaves out uncontested contests (no margin): 6 in 2022, 8 in 2024, 12 in 2026. "Targeted" means the whole contest was a formal target (coverage_status 'targeted'): 2022 Senate District 30; 2024 House District 10; 2026 House District 52 and Senate Districts 3, 20, 24. Every other legislative contest was audited opportunistically, on cards drawn for other targets, and has an opportunistic risk level computed from all cards examined in its counties, downsampled to the lowest county sampling rate. Median risk level of the contested legislative contests: 4.2% (2022), 14.2% (2024), 4.9% (2026). Cards examined: distinct cards in the comparison files (2024's 4,897 matches rlauxe's uniform count). 2026 figures are from round 2 data, computed 2026-11-22.

Cross-check, 2024: John's rlauxe-based risk levels (not yet published) cover 67 of the 75 contested legislative contests; 14 of them at or below 3%, median 26%. They are higher than ours because rlauxe's n leaves out cards drawn for the statewide targets, which our analysis now counts.

Estimated cards (an estimate, not an rlauxe run): no-discrepancy Kaplan-Markov sample size n = ln(0.03) / ln(1 − m / (2 × 1.03905)), the formula behind CORLA's own estimates (it reproduces the estMvrs column of risks-via-kotlin.csv). Style-based diluted margin m = margin in votes / contest_ballot_card_count (CORLA's count of cards carrying the contest), not the count of all cards in the contest's counties. The slide shows the upper end of a range: from the larger of the House sum and the Senate sum (House districts do not overlap, and Senate samples can reuse House-sampled cards) up to the sum of both. Ranges: 2022, 4,773 to 6,377; 2024, 3,555 to 5,186 (without the two recount-range contests); 2026, 3,184 to 3,903. Discrepancies would raise these numbers; the other targets' samples would still be needed, and would overlap these. The numbers come from a script of ours, not yet published.

2024 recount-range contests (margin at most 0.5% of the winner's votes): House District 16, 20,640 to 20,633 (7 votes; diluted margin 0.016% over its 44,231 cards, about 46,000 cards); House District 19, 28,417 to 28,294 (123 votes; 0.20%, about 3,600 cards). With them the 2024 upper figure is about 54,800.

House District 1 (2024, two counties): 10,071 votes; diluted margin 0.68% over the 1,472,050 cards in its counties, 26.4% over its own 38,105 cards. Our analysis counts 360 cards examined for it, giving an opportunistic risk level of 31%.

rlauxe simulation: https://github.com/JohnLCaron/rlauxe/blob/main/docs/cases/CorlaCounty2024.md ("Targeted contests plus important contests"; plot at https://johnlcaron.github.io/rlauxe/docs/cases/Corla24Dist/Corla24Dist-TargetPlus.html). Consistent sampling with card-style data, on CVRs simulated from county vote totals and card styles seen in the sampled cards: the targeted contests, all statewide contests, and contests whose names begin "State" or "Representative" needing fewer than 150 cards, in 4,792 cards, against 4,897 examined with uniform sampling. By the estimate above, 64 of the 75 contested 2024 legislative contests need fewer than 150 cards.

Prerequisite: a trusted upper bound on the cards carrying each contest, from card styles in the ballot manifest (the same rlauxe document, "CVRs vs Card Styles"). CORLA manifests do not carry card styles today.

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

[github.com/nealmcb/corla-observer](https://github.com/nealmcb/corla-observer)
[github.com/nealmcb/anonymize_cvr](https://github.com/nealmcb/anonymize_cvr)
[github.com/nealmcb/auditcenter](https://github.com/nealmcb/auditcenter)

[sites.google.com/view/auditenhancement](https://sites.google.com/view/auditenhancement)

<!-- analysis tables: start (make_table_slides.py) -->
---
class: table-slide, wide
### Table 1

| Election | Total contests | Targeted | Opportunistic | Single-county | Partial multi-county | Statewide |
|---|---:|---:|---:|---:|---:|---:|
| 2019 | 576 | 52 | 524 | 457 | 117 | 2 |
| 2020 (general) | 652 | 60 | 592 | 510 | 142 | 0 |
| 2020 (presidential) | 2 | 2 | 0 | 0 | 0 | 2 |
| 2020 (primary) | 372 | 34 | 338 | 282 | 87 | 3 |
| 2021 | 666 | 54 | 612 | 537 | 127 | 2 |
| 2022 (general) | 961 | 43 | 918 | 801 | 135 | 25 |
| 2022 (primary) | 651 | 38 | 613 | 543 | 96 | 12 |
| 2023 | 661 | 43 | 618 | 511 | 148 | 2 |
| 2024 | 721 | 63 | 658 | 555 | 142 | 24 |
| 2025 | 640 | 62 | 578 | 515 | 124 | 1 |
| 2026 (general) | 981 | 52 | 929 | 814 | 141 | 26 |
| 2026 (primary) | 620 | 26 | 594 | 512 | 97 | 11 |
| **Total** | **7,503** | **529** | **6,974** | **6,037** | **1,356** | **110** |

???
Caption: Targeted and opportunistic contests by election, and by county span.

From our analysis: Across the full survey (the table), **529 of 7,503 contests (7.1%) were targeted, and the other 6,974 (92.9%) were audited opportunistically**. Targeted contests are consistently a small minority of the total — never more than about 10% (setting aside the 2020 presidential primary, whose only two contests were both targeted), and 4 to 5% in the 2022 general and the 2026 primary and general, where the number of small down-ballot contests grows faster than the number of contests formally selected to drive sampling.

---
class: table-slide, wide
### Table 1, earlier version: of which no comparison row

| Election | Total contests | Targeted | Opportunistic | of which no comparison row | Single-county | Partial multi-county | Statewide |
|---|---:|---:|---:|---:|---:|---:|---:|
| 2019 | 576 | 52 | 524 | 22 | 457 | 117 | 2 |
| 2020 (general) | 652 | 60 | 592 | 66 | 510 | 142 | 0 |
| 2020 (presidential) | 2 | 2 | 0 | 0 | 0 | 0 | 2 |
| 2020 (primary) | 372 | 34 | 338 | 17 | 282 | 87 | 3 |
| 2021 | 666 | 54 | 612 | 21 | 537 | 127 | 2 |
| 2022 (general) | 961 | 43 | 918 | 37 | 801 | 135 | 25 |
| 2022 (primary) | 651 | 38 | 613 | 1 | 543 | 96 | 12 |
| 2023 | 661 | 43 | 618 | 69 | 511 | 148 | 2 |
| 2024 | 721 | 63 | 658 | 59 | 555 | 142 | 24 |
| 2025 | 640 | 62 | 578 | 30 | 515 | 124 | 1 |
| 2026 (general) | 981 | 52 | 929 | 53 | 814 | 141 | 26 |
| 2026 (primary) | 620 | 26 | 594 | 1 | 512 | 97 | 11 |
| **Total** | **7,503** | **529** | **6,974** | **376** | **6,037** | **1,356** | **110** |

???
Caption: Targeted and opportunistic contests by election, and by county span. "Of which no comparison row" is the part of the opportunistic count that no row of CORLA's comparison export names.

Contests by election (2019 through the 2026 general), from our analysis as of commit ab9dc04 of the analysis repository. This version splits out the opportunistic contests that no row of CORLA's comparison export names; every one of them still has an opportunistic risk level.

---
class: table-slide
### Table 2: Selection reproduction data: probably drop this slide

| Election | County-level targets | Statewide targets |
|---|---:|---:|
| 2019 | 63/63 | 1/1 |
| 2020 (general) | 63/63 | 3/3 |
| 2020 (presidential) | 0/0 | 2/2 |
| 2020 (primary) | 88/88 | 1/1 |
| 2021 | 63/64 | 1/1 |
| 2022 (primary) | 80/80 | 2/2 |
| 2022 (general) | 63/63 | 6/6 |
| 2023 | 63/63 | 1/1 |
| 2024 | 63/63 | 2/2 |
| 2025 | 73/73 | 2/2 |
| 2026 (primary) | 112/112 | 1/1 |
| 2026 (general) | 66/66 | 5/5 |

???
Caption: Selection-reproduction results by election.

From our analysis: Across the twelve election instances where the necessary files exist (the earliest three instances predate the file formats this check requires), **821 of 822 checkable targets — 99.9% — reproduce the audit software's own official selection exactly: zero ballots missing, zero extra**, for every target but one. Results by election appear in the table. This table counts targets, not deduplicated contests as in Table 1 — a single county-level contest name run independently by, say, twenty counties contributes twenty targets here, so the two tables' totals are not meant to be compared directly.

---
class: table-slide, wide
### Table 4: Discrepancy types

| Election | o2 | o1 | u1 | u2 | Total | Examined | Rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| 2018 general | 6 | 3 | 0 | 3 | 12 | 164,796 | 0.0073% |
| 2019 | 26 | 12 | 10 | 20 | 68 | 58,659 | 0.1159% |
| 2020 (primary) | 16 | 4 | 4 | 16 | 40 | 61,546 | 0.0650% |
| 2020 (general) | 59 | 68 | 85 | 47 | 259 | 234,333 | 0.1105% |
| 2020 (presidential) | 0 | 0 | 0 | 0 | 0 | 155 | 0.0000% |
| 2021 | 5 | 11 | 11 | 5 | 32 | 60,597 | 0.0528% |
| 2022 (primary) | 6 | 8 | 5 | 7 | 26 | 118,827 | 0.0219% |
| 2022 (general) | 54 | 39 | 36 | 24 | 153 | 233,223 | 0.0656% |
| 2023 | 5 | 3 | 9 | 2 | 19 | 35,486 | 0.0535% |
| 2024 | 47 | 52 | 71 | 55 | 225 | 149,272 | 0.1507% |
| 2025 | 4 | 6 | 4 | 3 | 17 | 47,706 | 0.0356% |
| 2026 (general) | 39 | 29 | 25 | 8 | 101 | 191,363 | 0.0528% |
| 2026 (primary) | 5 | 0 | 0 | 2 | 7 | 92,536 | 0.0076% |
| **Overall** | **272** | **235** | **260** | **192** | **959** | **1,448,499** | **0.0662%** |
| Overall rate | 0.0188% | 0.0162% | 0.0179% | 0.0133% | — | — | 0.0662% |

???
Caption: Two- and one-vote overstatement (o2/o1) and one- and two-vote understatement (u1/u2) discrepancy counts and rates by election; Total counts typed discrepancies only. The 2017 coordinated election and the 2018 primary have no comparison data; Table~\ref{tab:county-discrepancy-totals} gives CORLA's county totals for them.

From our analysis: Across every election with ballot-level comparison data (2018 general plus every "contest CSV"-era election, thirteen instances in all), **959 genuine, typed discrepancies were found across 1,448,499 examined contest-ballot comparisons, an overall rate of 0.066%** — broken down by Kaplan-Markov type and by election in the table.

---
class: table-slide
### Table 5: CORLA's untyped county totals, 2017 and the 2018 primary

| Election | Counties | Cards audited | Audited contests | Other contests | Total |
|---|---:|---:|---:|---:|---:|
| 2017 coordinated | 50 | 3,104 | 20 | 45 | 65 |
| 2018 (primary) | 58 | 7,971 | 17 | 74 | 91 |

???
Caption: Discrepancies in the 2017 coordinated election and the 2018 primary as CORLA's state audit reports count them, summed over each county's latest Round Summary block: ballot cards audited, and discrepancies in the county's audited contests and in its other contests. The counts are untyped and count a ballot card once in each group, so they are not comparable with the rates of Table~\ref{tab:discrepancy-typing-by-election}.

From our analysis: For the 2017 coordinated election and the 2018 primary, CORLA's state audit reports give only untyped county totals (the table): 65 discrepancies on 3,104 ballot cards audited in 50 counties in 2017, and 91 on 7,971 cards in 58 counties in the 2018 primary. CORLA's unit is not ours. For the 2022 general, which has both records, the state report's 7 discrepancies in audited contests and 52 in other contests are exactly the numbers of audited ballot cards with at least one genuine discrepancy in an audited contest and in any other contest; the same holds for the 2023 coordinated election and the 2026 primary. CORLA thus counts a card once in each group, however many of its contests disagree, where we count every contest: the 2022 general's 59 by CORLA's count are 186 genuine discrepancies (153 typed) by ours.

---
class: table-slide
### Table 6 (low importance): Secretary of State discrepancy reports, two transcriptions compared: to be reviewed, not included

| Election | Independently re-derived | Previously published | Gap |
|---|---:|---:|---:|
| 2020 (primary) | 119 | 122 | −3 |
| 2020 (general) | 276 | 280 | −4 |
| 2021 | 38 | 44 | −6 |
| 2022 (primary) | 86 | 93 | −7 |
| 2023 | 22 | 22 | exact |
| 2024 | 235 | 235 | exact |
| 2025 | 22 | 22 | exact |
| 2026 (primary) | 16 | 16 | exact |
| **Total** | **814** | **834** | **−20** |

???
Caption: Reconciliation of the independently re-derived discrepancy-report row counts against an earlier published tally of the same eight elections.

From our analysis: A from-scratch re-derivation of the same underlying Secretary of State reports, performed independently of an earlier published tally of the same eight elections, reproduces four of the eight exactly but comes up 20 rows short across the other four (814 versus 834 total, a 2.4% gap):

<!-- analysis tables: end -->
