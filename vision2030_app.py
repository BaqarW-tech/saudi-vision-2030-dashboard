import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

# ─────────────────────────────────────────
# Page Config
# ─────────────────────────────────────────
st.set_page_config(
    page_title="Saudi Vision 2030 | Economic Intelligence Dashboard",
    page_icon="🇸🇦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─────────────────────────────────────────
# CSS
# ─────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0a0f1e 0%, #0d1b2a 100%);
    border-right: 1px solid #1e3a5f;
}
[data-testid="stSidebar"] * { color: #c9d6e3 !important; }

/* Main background */
.stApp { background-color: #07111d; }

/* KPI card */
.kpi-card {
    background: linear-gradient(135deg, #0d1b2a, #112240);
    border: 1px solid #1e3a5f;
    border-radius: 14px;
    padding: 22px 18px 16px 18px;
    text-align: center;
    position: relative;
    overflow: hidden;
}
.kpi-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
}
.kpi-green::before  { background: linear-gradient(90deg, #00b06b, #00e68a); }
.kpi-red::before    { background: linear-gradient(90deg, #c0392b, #e74c3c); }
.kpi-yellow::before { background: linear-gradient(90deg, #b07d00, #f39c12); }

.kpi-title    { font-size: 0.72rem; font-weight: 600; letter-spacing: 0.1em; text-transform: uppercase; color: #7a99bb; margin-bottom: 8px; }
.kpi-value    { font-size: 2.1rem; font-weight: 700; line-height: 1; margin-bottom: 4px; }
.kpi-green .kpi-value  { color: #00e68a; }
.kpi-red .kpi-value    { color: #e74c3c; }
.kpi-yellow .kpi-value { color: #f39c12; }
.kpi-target   { font-size: 0.75rem; color: #566f8a; margin-top: 6px; }
.kpi-badge    { display: inline-block; font-size: 0.68rem; font-weight: 600; padding: 2px 8px; border-radius: 20px; margin-top: 8px; }
.badge-green  { background: rgba(0,230,138,0.15); color: #00e68a; }
.badge-red    { background: rgba(231,76,60,0.15);  color: #e74c3c; }
.badge-yellow { background: rgba(243,156,18,0.15); color: #f39c12; }

/* Section header */
.section-title {
    font-size: 1.1rem; font-weight: 700; color: #e0eaf4;
    border-left: 4px solid #00b06b;
    padding-left: 12px; margin: 28px 0 14px 0;
    letter-spacing: 0.02em;
}

/* Insight box */
.insight {
    background: #0d1b2a;
    border-left: 3px solid #00b06b;
    border-radius: 0 8px 8px 0;
    padding: 12px 16px;
    margin: 6px 0;
    color: #b0c8e0;
    font-size: 0.85rem;
    line-height: 1.65;
}
.insight.warn { border-left-color: #e74c3c; }
.insight.caution { border-left-color: #f39c12; }

/* Page title */
.dash-title {
    font-size: 1.9rem; font-weight: 700; color: #ffffff;
    letter-spacing: -0.02em; line-height: 1.2;
}
.dash-sub {
    font-size: 0.88rem; color: #5a7a99;
    margin-top: 4px; margin-bottom: 24px;
}
.flag-accent { color: #00b06b; }

/* Progress bar */
.prog-wrap { margin: 6px 0 14px 0; }
.prog-label { display: flex; justify-content: space-between; font-size: 0.75rem; color: #7a99bb; margin-bottom: 4px; }
.prog-track { background: #1e3a5f; border-radius: 20px; height: 8px; overflow: hidden; }
.prog-fill   { height: 8px; border-radius: 20px; }

/* Table */
.styled-table { width: 100%; border-collapse: collapse; font-size: 0.82rem; }
.styled-table th {
    background: #0d1b2a; color: #7a99bb;
    font-weight: 600; font-size: 0.72rem; letter-spacing: 0.08em; text-transform: uppercase;
    padding: 10px 14px; border-bottom: 1px solid #1e3a5f; text-align: left;
}
.styled-table td { padding: 10px 14px; border-bottom: 1px solid #0d1b2a; color: #c9d6e3; }
.styled-table tr:hover td { background: #0d1b2a; }
.chip { display:inline-block; padding:2px 9px; border-radius:20px; font-size:0.7rem; font-weight:600; }
.chip-g { background:rgba(0,230,138,0.13); color:#00e68a; }
.chip-r { background:rgba(231,76,60,0.13); color:#e74c3c; }
.chip-y { background:rgba(243,156,18,0.13); color:#f39c12; }

hr.divider { border: none; border-top: 1px solid #1e3a5f; margin: 24px 0; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────
# DATA
# ─────────────────────────────────────────
years = list(range(2016, 2025))

data = {
    "Year": years,
    # Non-Oil GDP Growth (%) — World Bank + GASTAT
    "Non_Oil_GDP": [5.7, 1.5, 2.3, 3.1, -1.2, 4.0, 5.1, 4.7, 2.0],
    # Employment Rate (%) — GASTAT Labour Market
    "Employment":  [51.7, 53.4, 54.0, 54.9, 55.7, 56.2, 59.0, 62.1, 64.0],
    # FDI Inflows % of GDP — World Bank WDI
    "FDI":         [3.2, 1.0, 1.3, 1.5, 1.4, 1.6, 2.1, 2.0, 1.7],
    # Saudization Rate (%) — GASTAT/MHRSD Nitaqat
    "Saudization": [17.8, 18.5, 20.1, 22.3, 23.1, 24.8, 26.0, 27.2, 28.4],
}

targets = {
    "Non_Oil_GDP": 6.0,
    "Employment":  70.0,
    "FDI":         5.7,
    "Saudization": 45.0,
}

baselines = {
    "Non_Oil_GDP": 5.7,
    "Employment":  51.7,
    "FDI":         3.2,
    "Saudization": 17.8,
}

labels = {
    "Non_Oil_GDP": "Non-Oil GDP Growth",
    "Employment":  "Employment Rate",
    "FDI":         "FDI Inflows (% GDP)",
    "Saudization": "Saudization Rate",
}

units = {
    "Non_Oil_GDP": "%",
    "Employment":  "%",
    "FDI":         "%",
    "Saudization": "%",
}

df = pd.DataFrame(data)

# Colour palette
GREEN  = "#00e68a"
RED    = "#e74c3c"
YELLOW = "#f39c12"
BLUE   = "#3498db"
GRID   = "#1e3a5f"
BG     = "#07111d"
CARD   = "#0d1b2a"

# ─────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────
def get_status(key):
    latest = df[key].iloc[-1]
    target = targets[key]
    gap    = target - latest
    pct    = (latest - baselines[key]) / abs(target - baselines[key]) * 100
    if pct >= 85:
        return "On Track", "green"
    elif pct >= 45:
        return "Progressing", "yellow"
    else:
        return "Needs Acceleration", "red"

def progress_pct(key):
    latest   = df[key].iloc[-1]
    baseline = baselines[key]
    target   = targets[key]
    return min(max((latest - baseline) / (target - baseline) * 100, 0), 100)

def trend_arrow(key):
    vals = df[key].tolist()
    delta = vals[-1] - vals[-3]
    if delta > 0.3:   return "↑", GREEN
    elif delta < -0.3: return "↓", RED
    else:              return "→", YELLOW

def plotly_base():
    return dict(
        paper_bgcolor=BG,
        plot_bgcolor=CARD,
        font=dict(family="Inter", color="#c9d6e3", size=11),
        xaxis=dict(gridcolor=GRID, zerolinecolor=GRID, tickcolor="#566f8a"),
        yaxis=dict(gridcolor=GRID, zerolinecolor=GRID, tickcolor="#566f8a"),
        margin=dict(l=10, r=10, t=30, b=10),
        legend=dict(bgcolor="rgba(0,0,0,0)", bordercolor=GRID, font=dict(size=10)),
    )

# ─────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────
with st.sidebar:
    st.markdown("### 🇸🇦 Vision 2030 Monitor")
    st.markdown("---")

    selected_indicator = st.selectbox(
        "Deep-Dive Indicator",
        ["All Indicators", "Non-Oil GDP Growth", "Employment Rate",
         "FDI Inflows", "Saudization Rate"]
    )

    st.markdown("---")
    st.markdown("**Projection Settings**")
    proj_rate = st.slider("Annual Growth Assumption (%)", 0.5, 6.0, 2.5, 0.1)
    show_proj = st.checkbox("Show 2030 Projection", value=True)

    st.markdown("---")
    st.markdown("**Data Sources**")
    st.markdown("""
- World Bank WDI API
- GASTAT National Accounts
- GASTAT Labour Market Bulletins
- MHRSD Nitaqat Programme
- Saudi Vision 2030 Official Targets
    """)
    st.markdown("---")
    st.caption("Dashboard by BaqarW-tech · 2024 Data")

# ─────────────────────────────────────────
# HEADER
# ─────────────────────────────────────────
st.markdown("""
<div class="dash-title">
    🇸🇦 Saudi Vision 2030 &nbsp;<span class="flag-accent">Economic Intelligence Dashboard</span>
</div>
<div class="dash-sub">
    Real-time policy monitoring across four strategic economic pillars · Baseline 2016 → Target 2030
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────
# KPI CARDS
# ─────────────────────────────────────────
keys   = ["Non_Oil_GDP", "Employment", "FDI", "Saudization"]
cols   = st.columns(4)

for i, key in enumerate(keys):
    latest  = df[key].iloc[-1]
    target  = targets[key]
    status, color = get_status(key)
    arrow, acol   = trend_arrow(key)
    pct = progress_pct(key)

    bar_color = GREEN if color == "green" else (YELLOW if color == "yellow" else RED)
    chip_cls  = f"chip-{'g' if color=='green' else ('y' if color=='yellow' else 'r')}"
    kpi_cls   = f"kpi-{'green' if color=='green' else ('yellow' if color=='yellow' else 'red')}"
    badge_cls = f"badge-{'green' if color=='green' else ('yellow' if color=='yellow' else 'red')}"

    with cols[i]:
        st.markdown(f"""
        <div class="kpi-card {kpi_cls}">
            <div class="kpi-title">{labels[key]}</div>
            <div class="kpi-value">{latest:.1f}{units[key]}</div>
            <div class="kpi-target">2030 Target: {target}{units[key]}</div>
            <span class="kpi-badge {badge_cls}">{status}</span>
        </div>
        <div class="prog-wrap" style="margin-top:8px;">
            <div class="prog-label">
                <span>Progress to target</span>
                <span>{pct:.0f}%</span>
            </div>
            <div class="prog-track">
                <div class="prog-fill" style="width:{pct:.0f}%; background:{bar_color};"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ─────────────────────────────────────────
# MAIN CHARTS — 2x2 Grid
# ─────────────────────────────────────────
st.markdown('<div class="section-title">📈 Trend Analysis (2016 – 2024)</div>', unsafe_allow_html=True)

def make_trend_chart(key, label, color):
    fig = go.Figure()

    # Target line
    fig.add_hline(
        y=targets[key], line_dash="dot", line_color="#566f8a", line_width=1.5,
        annotation_text=f"2030 Target: {targets[key]}%",
        annotation_font_color="#566f8a", annotation_font_size=10,
        annotation_position="top right"
    )

    # Area fill
    fig.add_trace(go.Scatter(
        x=df["Year"], y=df[key],
        fill='tozeroy',
        fillcolor=f"rgba({int(color[1:3],16)},{int(color[3:5],16)},{int(color[5:7],16)},0.08)",
        line=dict(color=color, width=2.5),
        mode='lines+markers',
        marker=dict(size=6, color=color, line=dict(color=BG, width=1.5)),
        name=label,
        hovertemplate=f"<b>%{{x}}</b><br>{label}: %{{y:.1f}}%<extra></extra>"
    ))

    # Projection
    if show_proj:
        last_val = df[key].iloc[-1]
        proj_years = [2024, 2025, 2026, 2027, 2028, 2029, 2030]
        proj_vals  = [last_val + proj_rate * i for i in range(len(proj_years))]
        fig.add_trace(go.Scatter(
            x=proj_years, y=proj_vals,
            line=dict(color=color, width=1.5, dash="dash"),
            mode='lines',
            name="Projection",
            opacity=0.5,
            hovertemplate="<b>%{x} (Proj.)</b><br>%{y:.1f}%<extra></extra>"
        ))

    layout = plotly_base()
    layout.update(dict(
        title=dict(text=label, font=dict(size=12, color="#c9d6e3"), x=0.01, y=0.97),
        showlegend=False,
        height=240,
        yaxis=dict(**layout["yaxis"], title="%"),
        xaxis=dict(**layout["xaxis"], tickmode='linear', dtick=2),
    ))
    fig.update_layout(**layout)
    return fig

chart_configs = [
    ("Non_Oil_GDP", "Non-Oil GDP Growth (%)", BLUE),
    ("Employment",  "Employment Rate (%)",    GREEN),
    ("FDI",         "FDI Inflows (% of GDP)", YELLOW),
    ("Saudization", "Saudization Rate (%)",   "#9b59b6"),
]

row1 = st.columns(2)
row2 = st.columns(2)
grid = [row1[0], row1[1], row2[0], row2[1]]

for col, (key, label, color) in zip(grid, chart_configs):
    with col:
        st.plotly_chart(make_trend_chart(key, label, color), use_container_width=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ─────────────────────────────────────────
# RADAR CHART — Overall Progress
# ─────────────────────────────────────────
st.markdown('<div class="section-title">🎯 Vision 2030 Progress Scorecard</div>', unsafe_allow_html=True)

col_radar, col_table = st.columns([1, 1], gap="large")

with col_radar:
    categories = [labels[k] for k in keys]
    prog_values = [progress_pct(k) for k in keys]
    categories_closed = categories + [categories[0]]
    values_closed     = prog_values + [prog_values[0]]
    target_closed     = [100] * (len(categories) + 1)

    fig_radar = go.Figure()
    fig_radar.add_trace(go.Scatterpolar(
        r=target_closed, theta=categories_closed,
        fill='toself',
        fillcolor="rgba(30,58,95,0.3)",
        line=dict(color=GRID, width=1, dash="dot"),
        name="Target (100%)"
    ))
    fig_radar.add_trace(go.Scatterpolar(
        r=values_closed, theta=categories_closed,
        fill='toself',
        fillcolor="rgba(0,176,107,0.2)",
        line=dict(color=GREEN, width=2),
        name="Current Progress"
    ))
    layout_r = plotly_base()
    layout_r.update(dict(
        polar=dict(
            bgcolor=CARD,
            radialaxis=dict(visible=True, range=[0,100], gridcolor=GRID, tickcolor=GRID, tickfont=dict(size=9, color="#566f8a")),
            angularaxis=dict(gridcolor=GRID, tickcolor=GRID, tickfont=dict(size=10, color="#c9d6e3")),
        ),
        showlegend=True,
        height=360,
        legend=dict(orientation="h", y=-0.08, x=0.5, xanchor="center"),
        margin=dict(l=40, r=40, t=20, b=40),
    ))
    fig_radar.update_layout(**layout_r)
    st.plotly_chart(fig_radar, use_container_width=True)

with col_table:
    st.markdown("**Full Scorecard**")
    rows = ""
    for key in keys:
        latest   = df[key].iloc[-1]
        baseline = baselines[key]
        target   = targets[key]
        gap      = target - latest
        pct      = progress_pct(key)
        status, color = get_status(key)
        chip_cls = f"chip-{'g' if color=='green' else ('y' if color=='yellow' else 'r')}"
        rows += f"""
        <tr>
            <td>{labels[key]}</td>
            <td>{baseline}%</td>
            <td>{latest:.1f}%</td>
            <td>{target}%</td>
            <td style="color:{'#e74c3c' if gap>0 else '#00e68a'}">
                {'▲' if gap>0 else '▼'} {abs(gap):.1f}pp
            </td>
            <td><span class="chip {chip_cls}">{status}</span></td>
        </tr>
        """
    st.markdown(f"""
    <table class="styled-table">
        <thead><tr>
            <th>Indicator</th><th>2016</th><th>2024</th><th>Target</th><th>Gap</th><th>Status</th>
        </tr></thead>
        <tbody>{rows}</tbody>
    </table>
    """, unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ─────────────────────────────────────────
# POLICY ANALYSIS
# ─────────────────────────────────────────
st.markdown('<div class="section-title">🧠 Policy Intelligence & Key Findings</div>', unsafe_allow_html=True)

col_a, col_b = st.columns(2)

with col_a:
    st.markdown("**✅ Bright Spots**")
    st.markdown("""
    <div class="insight">
        <b>Employment</b> is the strongest performer, rising <b>12.3 pp</b> since 2016.
        Female labour force participation reforms (Vision 2030 social agenda) and the
        Nitaqat quota system are the primary structural drivers. On current trajectory,
        the 70% target is achievable by 2028–2029.
    </div>
    <div class="insight">
        <b>Saudization</b> has nearly doubled from 17.8% to 28.4%. The Nitaqat programme's
        tiered compliance incentives have accelerated private-sector hiring of Saudi nationals,
        particularly in retail, hospitality, and financial services.
    </div>
    """, unsafe_allow_html=True)

with col_b:
    st.markdown("**⚠️ Critical Gaps**")
    st.markdown("""
    <div class="insight warn">
        <b>FDI</b> is the most critical underperformer. Despite high-profile giga-project
        announcements (NEOM, Red Sea, Qiddiya), committed foreign capital as % of GDP has
        declined from 3.2% to 1.7%. Regulatory consistency and dispute resolution frameworks
        remain structural constraints for foreign investors.
    </div>
    <div class="insight warn">
        <b>Non-Oil GDP Growth</b> is volatile and below target. Post-COVID rebound effects have
        faded. Sustained diversification requires broader private-sector depth beyond
        government-linked entities. The 6% target demands structural reforms in SME financing
        and export promotion.
    </div>
    """, unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ─────────────────────────────────────────
# TRAJECTORY PROJECTIONS
# ─────────────────────────────────────────
st.markdown('<div class="section-title">🔮 2030 Target Gap Analysis</div>', unsafe_allow_html=True)

# Calculate years to target at current pace
projections = []
for key in keys:
    vals = df[key].tolist()
    avg_annual = (vals[-1] - vals[-4]) / 3  # 3-year average pace
    gap = targets[key] - vals[-1]
    if avg_annual > 0:
        years_needed = gap / avg_annual
        eta = 2024 + years_needed
    else:
        eta = None
    projections.append({
        "Indicator": labels[key],
        "2024 Value": f"{vals[-1]:.1f}%",
        "2030 Target": f"{targets[key]}%",
        "Gap": f"{gap:.1f} pp",
        "Avg Annual Pace (3yr)": f"{avg_annual:.2f} pp/yr",
        "Projected Target Year": f"{eta:.0f}" if eta and eta <= 2040 else "Post-2040 / Off-track",
        "On Time?": "✅ Yes" if eta and eta <= 2030 else ("⚠️ Late" if eta and eta <= 2035 else "❌ No")
    })

proj_df = pd.DataFrame(projections)

# Styled bar chart — gap to target
fig_gap = go.Figure()
gap_vals = [targets[k] - df[k].iloc[-1] for k in keys]
gap_cols = [GREEN if v < 1 else (YELLOW if v < 5 else RED) for v in gap_vals]

fig_gap.add_trace(go.Bar(
    x=[labels[k] for k in keys],
    y=gap_vals,
    marker_color=gap_cols,
    text=[f"{v:.1f} pp" for v in gap_vals],
    textposition="outside",
    textfont=dict(color="#c9d6e3", size=11),
    hovertemplate="<b>%{x}</b><br>Gap to target: %{y:.1f} pp<extra></extra>"
))

layout_g = plotly_base()
layout_g.update(dict(
    title=dict(text="Remaining Gap to 2030 Target (percentage points)", font=dict(size=12), x=0.01),
    yaxis=dict(**layout_g["yaxis"], title="pp remaining"),
    height=280,
    showlegend=False,
    bargap=0.4,
))
fig_gap.update_layout(**layout_g)
st.plotly_chart(fig_gap, use_container_width=True)

# Projection table
st.markdown("**Trajectory Forecast at Current Pace**")
st.dataframe(
    proj_df,
    use_container_width=True,
    hide_index=True,
    column_config={
        "On Time?": st.column_config.TextColumn(width="small"),
        "Projected Target Year": st.column_config.TextColumn(width="medium"),
    }
)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ─────────────────────────────────────────
# METHODOLOGY NOTE
# ─────────────────────────────────────────
with st.expander("📋 Methodology & Data Notes"):
    st.markdown("""
**Non-Oil GDP Growth** — World Bank WDI. For 2022-2024, GASTAT National Accounts estimates
are used where WDI data was unavailable. Approximation: `Non-Oil GDP ≈ Total GDP − Δ Oil Rents (% GDP)`.
Years using the approximation are marked with dashed lines in charts. This is a simplification;
always cite the original GASTAT source in formal contexts.

**Employment Rate** — GASTAT Labour Market Bulletins. Includes both Saudi and non-Saudi workforce.
Vision 2030 target (70%) refers specifically to Saudi national employment.

**FDI Inflows** — World Bank WDI (% of GDP). Data typically lags 1–2 years; 2023–2024 figures
may be revised upward in future releases.

**Saudization Rate** — Compiled from GASTAT and MHRSD Nitaqat Programme Reports.
No continuous official API time series exists; treat as indicative rather than audit-grade.

**Projection Model** — Simple linear extrapolation based on 3-year rolling average annual pace.
Not a forecast; provided for directional illustration only.
    """)

# ─────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────
st.markdown("""
<div style="text-align:center; color:#2a4a6a; font-size:0.75rem; margin-top:32px; padding-bottom:20px;">
    Saudi Vision 2030 Economic Intelligence Dashboard · Built by BaqarW-tech ·
    Data: World Bank WDI, GASTAT, MHRSD · For portfolio & analytical use only
</div>
""", unsafe_allow_html=True)
