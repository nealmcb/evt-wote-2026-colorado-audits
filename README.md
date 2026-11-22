# EVT/WOTE 2026 talk: Evidence and Best Practices from Colorado Audits

Live deck: https://neal.mcburnett.org/elections/evt-wote-2026-colorado-audits/

**Do not trust any of this yet.** The slides, notes and chart are a draft that has had almost no
review. They were drafted with Claude, which repeatedly restated points it had misunderstood, for
example about which contests were targeted. The numbers rest on complicated notions that are easy
to get wrong:

- CORLA's targets include county portions of multi-county contests, each sized on one county's
  margin alone; a county portion is a target, but it does not make the contest a targeted contest.
- Contests that no row of CORLA's comparison export names are still opportunistic contests, with
  opportunistic risk levels; they are not unaudited or unknown.
- The state's exports have missing and inconsistent data, which the counts depend on.

Check every figure against our analysis and data before using it.

## What is here

A draft of the 15-minute talk for EVT/WOTE 2026, as a [remark.js](https://remarkjs.com) slide
deck:

- `slides.md`: the slides, with speaker notes after each `???`. The last slides, between the
  `analysis tables` markers, are the tables of our analysis.
- `slides.css`: the deck's styles; `index.html` loads remark.js (from remarkjs.com, so viewing
  needs a network connection) and `slides.md`.
- `make_contests_chart.py`: writes `contests.svg`, the chart on slide 4 (contests per election,
  targeted and opportunistic). Its numbers are copied into the script from Table 1 of
  our analysis (the analysis and its data are not yet published); its docstring says which build.
- `make_table_slides.py`: copies the tables of our analysis (its Markdown sections,
  `0*.md` in the folder given with `--sections`) into `slides.md` as appendix slides, with each table's caption and
  explanation in the speaker notes. Re-run it whenever the analysis's tables change.

Both scripts use only the Python standard library:

```
python3 make_contests_chart.py
python3 make_table_slides.py --sections PATH/TO/sections
```

## Viewing and rendering

Serve the folder and open it in a browser:

```
python3 -m http.server 8000
```

then visit http://localhost:8000/ and press `p` for the presenter view with notes. The
`view-presentation` script does the same, but it first kills every Python HTTP server
already running.

To make a PDF, with the server running:

```
decktape http://localhost:8000/#1 evt-wote-2026.pdf
```

To check one slide for overflow (remark.js cuts off text that does not fit; it does not shrink
it), screenshot it, here slide 4:

```
google-chrome --headless=new --window-size=1024,768 --virtual-time-budget=6000 --screenshot=slide-4.png "http://localhost:8000/#4"
```
