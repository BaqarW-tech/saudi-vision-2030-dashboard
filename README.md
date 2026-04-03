# 🇸🇦 Saudi Vision 2030 — Economic Intelligence Dashboard

> A professional-grade policy monitoring dashboard tracking Saudi Arabia's progress toward Vision 2030 targets across four strategic economic pillars — built with Python, Streamlit, and Plotly.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://saudi-vision-2030-dashboard-gupgdfxcdh4iubreuqznmw.streamlit.app/)

---

## 🔴 Live Demo

👉 **[Launch Dashboard](https://saudi-vision-2030-dashboard-gupgdfxcdh4iubreuqznmw.streamlit.app/)**

---

## 📊 What This Dashboard Does

This is not a static chart. It is an interactive economic intelligence tool that:

- Tracks **4 Vision 2030 KPIs** against official 2030 targets in real time
- Shows **RAG status** (On Track / Progressing / Needs Acceleration) per indicator
- Visualises **progress-to-target** with percentage bars for each pillar
- Renders a **radar chart** showing overall Vision 2030 achievement profile
- Calculates **projected target year** at current annual pace for each indicator
- Displays a **gap analysis bar chart** showing remaining distance to each target
- Includes an interactive **2030 projection toggle** with adjustable growth assumptions
- Provides a **policy intelligence section** with analyst-grade findings per pillar
- Contains full **methodology and data limitation notes** for academic credibility

---

## 📌 Indicators Tracked

| Indicator | Baseline (2016) | Latest (2024) | 2030 Target | Status |
|---|---|---|---|---|
| Non-Oil GDP Growth | 5.7% | 2.0% | 6.0% | ⚠️ Needs Acceleration |
| Employment Rate | 51.7% | 64.0% | 70.0% | ✅ On Track |
| FDI Inflows (% of GDP) | 3.2% | 1.7% | 5.7% | ❌ Needs Acceleration |
| Saudization Rate | 17.8% | 28.4% | 45.0% | ⚠️ Needs Acceleration |

---

## 🧠 Key Findings

**Employment** is the strongest performer, rising 12.3 percentage points since 2016. Female labour force participation reforms and the Nitaqat quota system are the primary structural drivers. On current trajectory, the 70% target is achievable by 2028–2029 — the only indicator on pace.

**Saudization** has nearly doubled from 17.8% to 28.4%, driven by Nitaqat compliance incentives in retail, hospitality, and financial services. However, at ~1.3 pp/year, the 45% target would not be reached until 2037 — seven years late.

**FDI** is the most critical underperformer. Despite high-profile giga-project announcements (NEOM, Red Sea, Qiddiya), committed foreign capital as % of GDP has declined from 3.2% to 1.7%. Regulatory consistency and dispute resolution frameworks remain structural constraints.

**Non-Oil GDP Growth** is volatile and below target. Post-COVID rebound effects have faded. Sustained diversification requires broader private-sector depth beyond government-linked entities.

---

## 🛠️ Tech Stack

| Component | Tool |
|---|---|
| Web Framework | Streamlit |
| Data Visualisation | Plotly (Graph Objects) |
| Data Processing | Pandas, NumPy |
| Styling | Custom CSS (Inter font, dark theme) |
| Deployment | Streamlit Cloud |

---

## 📂 Project Structure

```
saudi-vision-2030-dashboard/
│
├── vision2030_app.py               # Main Streamlit app
├── requirements.txt                # Python dependencies
├── Saudi_Vision_2030_Dashboard.ipynb  # Original Colab notebook
└── README.md                       # This file
```

---

## 🚀 Run Locally

```bash
# Clone the repo
git clone https://github.com/BaqarW-tech/saudi-vision-2030-dashboard.git
cd saudi-vision-2030-dashboard

# Install dependencies
pip install -r requirements.txt

# Launch the app
streamlit run vision2030_app.py
```

---

## 📋 Data Sources

| Indicator | Source |
|---|---|
| Non-Oil GDP Growth | World Bank WDI + GASTAT National Accounts |
| Employment Rate | GASTAT Labour Market Bulletins |
| FDI Inflows | World Bank WDI API |
| Saudization Rate | GASTAT / MHRSD Nitaqat Programme Reports |
| 2030 Targets | Saudi Vision 2030 Official Programme |

---

## ⚠️ Methodology Notes

**Non-Oil GDP** — Approximated as `Total GDP Growth − Δ Oil Rents (% of GDP)` where direct data was unavailable. GASTAT National Accounts estimates used for 2022–2024.

**Saudization** — No continuous official API time series exists. Figures compiled from GASTAT and MHRSD press releases. Treat as indicative rather than audit-grade.

**FDI** — World Bank data typically lags 1–2 years. 2023–2024 figures may be revised upward in future releases.

**Projection Model** — Simple linear extrapolation based on 3-year rolling average. Not a forecast; provided for directional illustration only.

---

## 👤 About

**Author:** Mor Wagan
**Education:** MA Economics
**Focus:** Economic analysis, policy evaluation, and data-driven research targeting finance and public sector roles aligned with Saudi Vision 2030 — including institutions such as the Islamic Development Bank, SAMA, and UN agencies operating in the MENA region.

This project demonstrates applied skills in Python data analytics, interactive dashboard development, use of international economic databases, methodology transparency, and policy communication.

---

## 📄 License

MIT License — free to use with attribution.
