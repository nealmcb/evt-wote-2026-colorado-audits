#!/usr/bin/env python3
"""Write contests.svg: contests per Colorado election, targeted and opportunistic.

Written 2026-11-21 for the EVT/WOTE 2026 talk. The numbers are our analysis's
contest coverage counts (its Table 1), computed that day from the cross-election database
behind it, which we may publish, rebuilt with the 2026 general onboarded (2026 general
files from the auditcenter mirror at commit 357c682). Two bands: targeted contests (the whole
contest was a formal target) and opportunistic contests (every other contest, audited on
cards drawn for other targets; a contest whose only targets were county portions, each sized
on one county's margin, is opportunistic). Every opportunistic contest has an opportunistic
risk level. 2017-2018 (ballot-list era) are not in that table, and the 2020
presidential primary's 2 contests are left out of the chart. Colours are Okabe-Ito blue and
orange, readable with red-green colour blindness; the legend also labels each band in text.
Standard library only.
"""

from pathlib import Path

ROWS = [  # election, targeted, opportunistic
    ("2019", 52, 524),
    ("2020 primary", 34, 338),
    ("2020 general", 60, 592),
    ("2021", 54, 612),
    ("2022 primary", 38, 613),
    ("2022 general", 43, 918),
    ("2023", 43, 618),
    ("2024 general", 63, 658),
    ("2025", 62, 578),
    ("2026 primary", 26, 594),
    ("2026 general", 52, 929),
]
COLOURS = [
    ("Targeted", "#0072B2"),
    ("Opportunistic", "#E69F00"),
]

W, H = 760, 460
LEFT, RIGHT, TOP, BOTTOM = 70, 70, 70, 90
plot_w, plot_h = W - LEFT - RIGHT, H - TOP - BOTTOM
top_value = 1000
bar_w = plot_w / len(ROWS) * 0.7
step = plot_w / len(ROWS)


def y(v: float) -> float:
    return TOP + plot_h * (1 - v / top_value)


parts = [
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
    'font-family="Helvetica, Arial, sans-serif">',
    f'<text x="{LEFT}" y="28" font-size="20" font-weight="bold">Contests per election: targeted and opportunistic</text>',
]
for v in range(0, top_value + 1, 250):
    parts.append(f'<line x1="{LEFT}" x2="{W - RIGHT}" y1="{y(v):.1f}" y2="{y(v):.1f}" stroke="#dddddd"/>')
    parts.append(f'<text x="{LEFT - 8}" y="{y(v) + 5:.1f}" font-size="13" text-anchor="end">{v}</text>')
for i, (label, *values) in enumerate(ROWS):
    x = LEFT + i * step + (step - bar_w) / 2
    base = 0
    for v, (_, colour) in zip(values, COLOURS):
        parts.append(f'<rect x="{x:.1f}" y="{y(base + v):.1f}" width="{bar_w:.1f}" height="{y(base) - y(base + v):.1f}" fill="{colour}"/>')
        base += v
    parts.append(f'<text x="{x + bar_w / 2:.1f}" y="{y(base) - 6:.1f}" font-size="12" text-anchor="middle">{base}</text>')
    parts.append(
        f'<text transform="translate({x + bar_w / 2:.1f},{TOP + plot_h + 14}) rotate(35)" font-size="13">{label}</text>'
    )
lx = LEFT
for name, colour in COLOURS:
    parts.append(f'<rect x="{lx}" y="40" width="14" height="14" fill="{colour}"/>')
    parts.append(f'<text x="{lx + 20}" y="52" font-size="13">{name}</text>')
    lx += 20 + len(name) * 7.4 + 24
parts.append("</svg>")
Path(__file__).with_name("contests.svg").write_text("\n".join(parts) + "\n", encoding="utf-8")
print(
    "wrote contests.svg:",
    sum(sum(r[1:]) for r in ROWS), "contests,",
    sum(r[1] for r in ROWS), "targeted,",
    sum(r[2] for r in ROWS), "opportunistic",
)
