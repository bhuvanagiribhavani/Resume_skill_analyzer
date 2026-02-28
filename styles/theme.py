"""
styles — Custom CSS for both dark and light themes.
"""

# ── Shared base (font import, sidebar/toolbar hide, hero, toggle, common layout) ──
_BASE_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

[data-testid="stSidebar"] { display: none !important; }
[data-testid="stToolbar"] { display: none !important; }

.hero {
    text-align: center;
    padding: 48px 20px 24px;
}
.hero h1 {
    font-size: 2.2rem;
    font-weight: 700;
    margin: 0 0 6px;
}
.hero p {
    font-size: 1rem;
    margin: 0;
}

/* Toggle row */
.theme-toggle-row {
    display: flex;
    justify-content: flex-end;
    padding: 10px 24px 0;
}

/* Metric card shared structure */
[data-testid="stMetric"] {
    border-radius: 14px;
    padding: 22px 16px;
    text-align: center;
    transition: transform 0.2s, border-color 0.2s;
}
[data-testid="stMetric"]:hover {
    transform: translateY(-2px);
    border-color: #4db8a4;
}
[data-testid="stMetricLabel"] p {
    font-size: 0.78rem !important;
    text-transform: uppercase;
    letter-spacing: 1px;
}
[data-testid="stMetricValue"] {
    font-size: 1.7rem !important;
    font-weight: 700 !important;
}

/* Section title shared structure */
.sec-title {
    font-size: 1.25rem;
    font-weight: 600;
    margin: 2.2rem 0 0.9rem 0;
    padding-bottom: 0.45rem;
    display: flex;
    align-items: center;
    gap: 8px;
}
.sec-title .accent { color: #4db8a4; }

/* Skill chips shared structure */
.skill-chip {
    display: inline-block;
    padding: 7px 15px;
    margin: 4px;
    border-radius: 8px;
    font-size: 0.82rem;
    font-weight: 500;
    transition: border-color 0.15s, color 0.15s;
}
.skill-chip:hover {
    border-color: #4db8a4;
}

/* Domain block shared */
.domain-block {
    border-radius: 12px;
    padding: 18px 22px;
    margin-bottom: 14px;
}
.domain-label {
    color: #4db8a4;
    font-weight: 600;
    font-size: 0.95rem;
    margin-bottom: 10px;
}

/* Role card shared */
.role-card-primary {
    border-radius: 14px;
    padding: 28px 20px;
    text-align: center;
}
.role-card-primary h3 {
    margin: 0 0 6px;
    font-size: 1.35rem;
}
.role-card-primary p {
    margin: 0;
    font-size: 0.85rem;
}
.role-card-alt {
    border-radius: 10px;
    padding: 16px;
    text-align: center;
    font-weight: 500;
    font-size: 0.92rem;
    transition: border-color 0.15s;
}
.role-card-alt:hover {
    border-color: #4db8a4;
}

/* Progress bar accent */
[data-testid="stProgress"] > div > div {
    background: linear-gradient(90deg, #2d8a7a, #4db8a4) !important;
    border-radius: 8px;
}

/* Expander shared */
[data-testid="stExpander"] {
    border-radius: 12px;
}

/* File uploader shared */
[data-testid="stFileUploader"] {
    border-radius: 14px;
    padding: 20px;
    transition: border-color 0.2s;
}
[data-testid="stFileUploader"]:hover {
    border-color: #4db8a4;
}
"""

# ── Dark-only overrides ──
_DARK_OVERRIDES = """
html, body, [data-testid="stAppViewContainer"] {
    font-family: 'Inter', sans-serif;
    background: #111113 !important;
    color: #d4d4d4 !important;
}
[data-testid="stHeader"] { background: transparent !important; }

.hero h1 { color: #f5f5f5; }
.hero p   { color: #888; }

[data-testid="stMetric"] {
    background: #1a1a1d;
    border: 1px solid #2a2a2d;
}
[data-testid="stMetricLabel"] p { color: #777 !important; }
[data-testid="stMetricValue"]   { color: #e0e0e0 !important; }

.sec-title {
    color: #f0f0f0;
    border-bottom: 2px solid #2a2a2d;
}

.skill-chip {
    background: #1e1e21;
    color: #ccc;
    border: 1px solid #2e2e32;
}
.skill-chip:hover { color: #6dd4c0; }

.domain-block {
    background: #161618;
    border: 1px solid #222225;
}

.role-card-primary {
    background: linear-gradient(135deg, #15201d 0%, #1a1a1d 100%);
    border: 1px solid #2a3d38;
}
.role-card-primary h3 { color: #6dd4c0; }
.role-card-primary p  { color: #777; }

.role-card-alt {
    background: #1a1a1d;
    border: 1px solid #2a2a2d;
    color: #bbb;
}

[data-testid="stExpander"] {
    background: #161618;
    border: 1px solid #222225;
}

hr { border-color: #222225 !important; }

[data-testid="stFileUploader"] {
    background: #161618;
    border: 2px dashed #2e2e32;
}

/* Dark inline bars */
.bar-bg  { background: #1e1e21; }
.bar-fill { background: linear-gradient(90deg, #2d8a7a, #4db8a4); }
.bar-label { color: #ccc; }
.bar-count { color: #666; }
"""

# ── Light-only overrides ──
_LIGHT_OVERRIDES = """
html, body, [data-testid="stAppViewContainer"] {
    font-family: 'Inter', sans-serif;
    background: #f5f5f7 !important;
    color: #1a1a1d !important;
}
[data-testid="stHeader"] { background: #f5f5f7 !important; }

.hero h1 { color: #1a1a1d; }
.hero p   { color: #666; }

[data-testid="stMetric"] {
    background: #ffffff;
    border: 1px solid #e0e0e0;
    box-shadow: 0 1px 4px rgba(0,0,0,0.04);
}
[data-testid="stMetricLabel"] p { color: #888 !important; }
[data-testid="stMetricValue"]   { color: #1a1a1d !important; }

.sec-title {
    color: #1a1a1d;
    border-bottom: 2px solid #e0e0e0;
}

.skill-chip {
    background: #ffffff;
    color: #333;
    border: 1px solid #d5d5d5;
}
.skill-chip:hover { color: #2d8a7a; }

.domain-block {
    background: #ffffff;
    border: 1px solid #e4e4e4;
    box-shadow: 0 1px 3px rgba(0,0,0,0.03);
}

.role-card-primary {
    background: linear-gradient(135deg, #e8f5f1 0%, #ffffff 100%);
    border: 1px solid #c8e6df;
}
.role-card-primary h3 { color: #2d8a7a; }
.role-card-primary p  { color: #666; }

.role-card-alt {
    background: #ffffff;
    border: 1px solid #e0e0e0;
    color: #444;
}

[data-testid="stExpander"] {
    background: #ffffff;
    border: 1px solid #e4e4e4;
}

hr { border-color: #e0e0e0 !important; }

[data-testid="stFileUploader"] {
    background: #ffffff;
    border: 2px dashed #c8c8c8;
}

/* Light inline bars */
.bar-bg   { background: #e8e8e8; }
.bar-fill { background: linear-gradient(90deg, #3ca892, #4db8a4); }
.bar-label { color: #333; }
.bar-count { color: #888; }

/* Light-mode text colors for various Streamlit elements */
[data-testid="stMarkdownContainer"] p,
[data-testid="stMarkdownContainer"] li,
[data-testid="stMarkdownContainer"] span,
[data-testid="stText"] {
    color: #1a1a1d;
}
[data-testid="stExpanderToggleDetails"] p { color: #333 !important; }
"""


def get_theme_css(theme: str = "dark") -> str:
    """Return complete CSS wrapped in <style> for the chosen theme."""
    overrides = _DARK_OVERRIDES if theme == "dark" else _LIGHT_OVERRIDES
    return f"<style>{_BASE_CSS}\n{overrides}</style>"


# Chart colour palettes keyed by theme
CHART_COLORS = {
    "dark": {
        "pie_colors": ["#4db8a4", "#e07b6c", "#c4a6e0", "#e0c56a", "#6ab0b8", "#b8b8b8"],
        "pie_line": "#111113",
        "text": "#d4d4d4",
        "legend_text": "#888",
        "bar_scale": [[0, "#2d8a7a"], [1, "#4db8a4"]],
        "grid": "rgba(255,255,255,0.04)",
        "axis": "#777",
        "yaxis": "#bbb",
        "font": "#aaa",
    },
    "light": {
        "pie_colors": ["#4db8a4", "#e07b6c", "#b89ad6", "#d4a84e", "#5096a0", "#aaa"],
        "pie_line": "#f5f5f7",
        "text": "#333",
        "legend_text": "#555",
        "bar_scale": [[0, "#3ca892"], [1, "#4db8a4"]],
        "grid": "rgba(0,0,0,0.06)",
        "axis": "#666",
        "yaxis": "#333",
        "font": "#555",
    },
}
