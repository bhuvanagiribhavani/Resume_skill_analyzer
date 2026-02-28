"""
charts — Plotly chart builders for the analytics section (theme-aware).
"""

from collections import Counter

import plotly.graph_objects as go

from styles.theme import CHART_COLORS


# ---------------------------------------------------------------------------
# Pie Chart – Skill distribution by domain
# ---------------------------------------------------------------------------
def build_pie_chart(
    detected_skills: dict[str, list[str]],
    theme: str = "dark",
) -> go.Figure:
    """Donut chart of skill distribution, styled for the active theme."""
    pal = CHART_COLORS[theme]
    labels = list(detected_skills.keys())
    values = [len(v) for v in detected_skills.values()]

    fig = go.Figure(
        go.Pie(
            labels=labels,
            values=values,
            hole=0.45,
            marker=dict(
                colors=pal["pie_colors"][: len(labels)],
                line=dict(color=pal["pie_line"], width=2),
            ),
            textinfo="label+percent",
            textfont=dict(size=13, color=pal["text"]),
            hovertemplate=(
                "<b>%{label}</b><br>"
                "Skills: %{value}<br>"
                "Share: %{percent}<extra></extra>"
            ),
        )
    )
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color=pal["font"]),
        margin=dict(t=30, b=20, l=20, r=20),
        legend=dict(
            font=dict(color=pal["legend_text"], size=12),
            bgcolor="rgba(0,0,0,0)",
        ),
        height=380,
    )
    return fig


# ---------------------------------------------------------------------------
# Bar Chart – Skill mention frequencies
# ---------------------------------------------------------------------------
def build_bar_chart(
    frequencies: Counter,
    theme: str = "dark",
) -> go.Figure:
    """Horizontal bar chart of top skill mentions, styled for the active theme."""
    pal = CHART_COLORS[theme]
    sorted_items = frequencies.most_common(15)
    skills = [s for s, _ in reversed(sorted_items)]
    counts = [c for _, c in reversed(sorted_items)]

    fig = go.Figure(
        go.Bar(
            x=counts,
            y=skills,
            orientation="h",
            marker=dict(
                color=counts,
                colorscale=pal["bar_scale"],
                line=dict(width=0),
            ),
            hovertemplate="<b>%{y}</b>: %{x} mention(s)<extra></extra>",
        )
    )
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color=pal["font"], size=12),
        xaxis=dict(
            title="Mentions",
            gridcolor=pal["grid"],
            color=pal["axis"],
        ),
        yaxis=dict(color=pal["yaxis"]),
        margin=dict(t=20, b=40, l=10, r=20),
        height=max(280, len(skills) * 30 + 60),
    )
    return fig
