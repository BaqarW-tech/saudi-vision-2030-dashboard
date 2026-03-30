# Saudi Vision 2030 — Economic Indicators Dashboard

An interactive policy monitoring dashboard tracking Saudi Arabia's progress
toward Vision 2030 targets across four key economic indicators.

Built in Python (Google Colab) using live World Bank API data, supplemented
with GASTAT and MHRSD sources. Developed as a portfolio project demonstrating
data analysis, economic methodology, and policy evaluation skills.

---

## Indicators Tracked

| Indicator | Baseline (2016) | Latest (2024) | 2030 Target | Status |
|---|---|---|---|---|
| Non-Oil GDP Growth | 5.7% | 2.0% | 6.0% | ⚠️ Needs acceleration |
| Employment Rate | 51.7% | 64.0% | 70.0% | ✅ On track |
| FDI Inflows (% of GDP) | 3.2% | 1.7% | 5.7% | ⚠️ Needs acceleration |
| Saudization Rate | 17.8% | 28.4% | 45.0% | ⚠️ Needs acceleration |

---

## Key Findings

**Employment** is the strongest performer, rising 12.3 percentage points
since 2016 — driven by female labour force participation reforms and the
Nitaqat quota system. It is the only indicator on track to meet its 2030
target.

**Saudization** has nearly doubled from 17.8% to 28.4%, but at the current
pace of ~1.3 pp/year, the 45% target would not be reached until 2037 —
seven years late.

**FDI** is the most critical underperformer. Despite high-profile giga-project
announcements (NEOM, Red Sea, Qiddiya), committed foreign capital as a share
of GDP has declined. Investor uncertainty around regulatory consistency
remains a structural constraint.

**Non-Oil GDP Growth** is volatile and well below target. Post-COVID rebound
effects have faded; sustained diversification requires broader private-sector
depth beyond government-linked entities.

---

## Data Sources

| Indicator | Source |
|---|---|
| GDP growth, FDI, Employment | [World Bank WDI API](https://data.worldbank.org/) |
| Non-Oil GDP (2022–2024) | GASTAT National Accounts press releases |
| Saudization rate | GASTAT Labour Market Bulletins; MHRSD Nitaqat Programme Reports |

---

## Methodology Notes

### Non-Oil GDP Approximation
Non-oil GDP growth is not directly available via the World Bank API.
It is approximated as:

```
Non-Oil GDP Growth ≈ Total GDP Growth − Change in Oil Rents (% of GDP)
```

This is a simplification. Oil rents measure revenue, not sectoral output
directly. For 2022–2024, where World Bank oil rents data was unavailable,
figures were overridden with GASTAT National Accounts estimates.
Years using the approximation formula are flagged in the dashboard
with dashed lines and × markers.

### Saudization Data
No continuous official time series is freely accessible via API.
Figures are compiled from GASTAT and MHRSD press releases.
Treat as indicative rather than audit-grade. Always cite original
source when presenting in formal contexts.

### FDI Lag
World Bank FDI data typically lags actual inflows by 1–2 years.
2023–2024 figures may be revised upward in future releases.

---

## Tech Stack

- **Python 3** (Google Colab)
- **pandas** — data wrangling and scorecard table
- **matplotlib** — four-panel dashboard and charts
- **wbgapi** — World Bank API data fetch
- **Claude AI** — coding collaborator and methodology advisor

---

## How to Run

1. Open [Google Colab](https://colab.research.google.com/)
2. Upload `Saudi_Vision_2030_Dashboard.ipynb`
3. Run cells in order — the notebook fetches live World Bank data
   automatically
4. If `wbgapi` is not installed, the first cell installs it
5. Output: four-panel dashboard PNG + progress scorecard table +
   policy analysis brief

---

## About

**Author:** Mor Wagan
**Education:** MA Economics
**Focus:** Economic analysis, policy evaluation, and data-driven research
targeting finance and public sector roles in Saudi Arabia aligned with
Vision 2030.

This project demonstrates applied skills in Python data analysis, use of
international economic databases (World Bank WDI), methodology transparency,
and policy communication — built through structured collaboration with
Claude AI.

---

## Files

| File | Description |
|---|---|
| `Saudi_Vision_2030_Dashboard.ipynb` | Main notebook (all steps) |
| `vision2030_dashboard.png` | Exported dashboard chart |
| `README.md` | This file |
