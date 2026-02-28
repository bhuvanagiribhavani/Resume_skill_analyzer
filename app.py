"""
AI Resume Analyzer — Streamlit Entry Point
===========================================
Run with:  streamlit run app.py
"""

import streamlit as st

from config.skills_db import SKILLS_DB
from styles.theme import get_theme_css
from utils.analyzer import (
    extract_text,
    preprocess_text,
    extract_skills,
    count_skill_frequencies,
    calculate_strength_score,
    recommend_role,
)
from utils.charts import build_pie_chart, build_bar_chart


# ---------------------------------------------------------------------------
# Streamlit UI — single-page scrollable layout
# ---------------------------------------------------------------------------
def main() -> None:
    st.set_page_config(
        page_title="Resume Analyzer",
        page_icon="📄",
        layout="wide",
        initial_sidebar_state="collapsed",
    )

    # ---- Theme toggle ----
    if "theme" not in st.session_state:
        st.session_state["theme"] = "dark"

    # Right-aligned toggle row
    _, toggle_col = st.columns([6, 1])
    with toggle_col:
        is_light = st.toggle(
            "☀️ Light",
            value=(st.session_state["theme"] == "light"),
            key="_theme_toggle",
        )
    st.session_state["theme"] = "light" if is_light else "dark"
    theme = st.session_state["theme"]

    st.markdown(get_theme_css(theme), unsafe_allow_html=True)

    # ---- Hero + Upload ----
    st.markdown(
        "<div class='hero'>"
        "<h1>Resume Analyzer</h1>"
        "<p>Drop your resume below and scroll down for the full analysis.</p>"
        "</div>",
        unsafe_allow_html=True,
    )

    col_pad_l, col_upload, col_pad_r = st.columns([1, 2, 1])
    with col_upload:
        uploaded_file = st.file_uploader(
            "Upload your resume",
            type=["pdf", "docx", "txt"],
            help="Supported: PDF, DOCX, TXT",
            label_visibility="collapsed",
        )

    # ---- Guard: nothing uploaded yet ----
    if uploaded_file is None:
        placeholder_color = "#555" if theme == "dark" else "#999"
        st.markdown(
            f"<p style='text-align:center; color:{placeholder_color}; margin-top:60px; "
            "font-size:0.95rem;'>"
            "Upload a PDF, DOCX, or TXT resume to get started.</p>",
            unsafe_allow_html=True,
        )
        return

    # ---- Process file (cached in session state) ----
    file_id = f"{uploaded_file.name}_{uploaded_file.size}"
    if st.session_state.get("_file_id") != file_id:
        with st.spinner("Analyzing…"):
            try:
                raw_text = extract_text(uploaded_file)
            except Exception as exc:
                st.error(f"Error reading file: {exc}")
                return
            if not raw_text.strip():
                st.warning("No text could be extracted.")
                return

            cleaned = preprocess_text(raw_text)
            detected = extract_skills(cleaned)
            total_skills = sum(len(v) for v in detected.values())
            score = calculate_strength_score(detected)
            role_info = recommend_role(detected)
            frequencies = count_skill_frequencies(cleaned, detected)

            st.session_state.update(
                {
                    "_file_id": file_id,
                    "raw_text": raw_text,
                    "detected": detected,
                    "total_skills": total_skills,
                    "score": score,
                    "role_info": role_info,
                    "frequencies": frequencies,
                    "file_name": uploaded_file.name,
                }
            )

    # Unpack
    detected = st.session_state["detected"]
    total_skills = st.session_state["total_skills"]
    score = st.session_state["score"]
    role_info = st.session_state["role_info"]
    frequencies = st.session_state["frequencies"]
    raw_text = st.session_state["raw_text"]
    file_name = st.session_state["file_name"]

    # ==================================================================
    # 01 — Overview metrics
    # ==================================================================
    st.markdown(
        "<p class='sec-title'><span class='accent'>01</span> Overview</p>",
        unsafe_allow_html=True,
    )
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Skills", total_skills)
    c2.metric("Strength Score", f"{score}%")
    c3.metric("Domains", len(detected))
    c4.metric("Primary Role", role_info["primary"].split("/")[0].strip())

    # ==================================================================
    # 02 — Resume Strength
    # ==================================================================
    st.markdown(
        "<p class='sec-title'><span class='accent'>02</span> Resume Strength</p>",
        unsafe_allow_html=True,
    )
    st.progress(min(score / 100, 1.0))
    if score >= 70:
        st.success(f"Strong resume — {score}% strength.")
    elif score >= 40:
        st.warning(
            f"Moderate resume — {score}% strength. Consider adding more skills."
        )
    else:
        st.error(f"Weak resume — {score}% strength. Significant improvement needed.")

    # ==================================================================
    # 03 — Detected Skills
    # ==================================================================
    st.markdown(
        "<p class='sec-title'><span class='accent'>03</span> Detected Skills</p>",
        unsafe_allow_html=True,
    )
    if detected:
        for domain, skills in detected.items():
            chips = "".join(f"<span class='skill-chip'>{s}</span>" for s in skills)
            st.markdown(
                f"<div class='domain-block'>"
                f"<div class='domain-label'>{domain}  —  {len(skills)} skill(s)</div>"
                f"{chips}</div>",
                unsafe_allow_html=True,
            )
    else:
        st.info("No technical skills detected.")

    # ==================================================================
    # 04 — Analytics
    # ==================================================================
    st.markdown(
        "<p class='sec-title'><span class='accent'>04</span> Analytics</p>",
        unsafe_allow_html=True,
    )
    if detected:
        left, right = st.columns(2)
        with left:
            st.markdown(
                "<p style='color:#4db8a4; font-weight:600; font-size:0.95rem; "
                "margin-bottom:2px;'>Skill Distribution</p>",
                unsafe_allow_html=True,
            )
            st.plotly_chart(
                build_pie_chart(detected, theme=theme),
                width="stretch",
            )
        with right:
            st.markdown(
                "<p style='color:#4db8a4; font-weight:600; font-size:0.95rem; "
                "margin-bottom:2px;'>Top Mentions</p>",
                unsafe_allow_html=True,
            )
            st.plotly_chart(
                build_bar_chart(frequencies, theme=theme),
                width="stretch",
            )

    # ==================================================================
    # 05 — Recommended Roles
    # ==================================================================
    st.markdown(
        "<p class='sec-title'><span class='accent'>05</span> Recommended Roles</p>",
        unsafe_allow_html=True,
    )
    st.markdown(
        f"<div class='role-card-primary'>"
        f"<p style='color:#777; margin:0 0 4px; font-size:0.75rem; "
        f"text-transform:uppercase; letter-spacing:1px;'>Primary Recommendation</p>"
        f"<h3>{role_info['primary']}</h3>"
        f"<p>Based on: {role_info['dominant_domain']}</p>"
        f"</div>",
        unsafe_allow_html=True,
    )
    if role_info["alternatives"]:
        st.markdown("<br>", unsafe_allow_html=True)
        cols = st.columns(len(role_info["alternatives"]))
        for idx, alt in enumerate(role_info["alternatives"]):
            cols[idx].markdown(
                f"<div class='role-card-alt'>{alt}</div>",
                unsafe_allow_html=True,
            )

    # ==================================================================
    # 06 — Skill Breakdown
    # ==================================================================
    st.markdown(
        "<p class='sec-title'><span class='accent'>06</span> Skill Breakdown</p>",
        unsafe_allow_html=True,
    )
    for domain, skills in detected.items():
        with st.expander(f"{domain}  —  {len(skills)} skill(s)", expanded=False):
            for skill in skills:
                freq = frequencies.get(skill, 1)
                bar_pct = min(freq * 20, 100)
                st.markdown(
                    f"<div style='display:flex; align-items:center; margin:5px 0;'>"
                    f"<span class='bar-label' style='width:140px; font-weight:500;'>"
                    f"{skill}</span>"
                    f"<div class='bar-bg' style='flex:1; border-radius:6px; "
                    f"height:8px; margin:0 12px;'>"
                    f"<div class='bar-fill' style='width:{bar_pct}%; "
                    f"height:100%; border-radius:6px;'>"
                    f"</div></div>"
                    f"<span class='bar-count' style='font-size:0.82rem;'>×{freq}</span>"
                    f"</div>",
                    unsafe_allow_html=True,
                )

    # ==================================================================
    # 07 — Extracted Text
    # ==================================================================
    st.markdown(
        "<p class='sec-title'><span class='accent'>07</span> Extracted Text</p>",
        unsafe_allow_html=True,
    )
    with st.expander("Show resume text", expanded=False):
        st.text(raw_text[:5000] + ("…" if len(raw_text) > 5000 else ""))


if __name__ == "__main__":
    main()
