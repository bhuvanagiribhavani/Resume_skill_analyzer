"""
utils — Core analysis functions: extraction, preprocessing, skills, scoring, roles.
"""

import re
from collections import Counter

import PyPDF2
import docx

from config.skills_db import (
    SKILLS_DB,
    DISPLAY_NAME_OVERRIDES,
    SKILL_BENCHMARK,
    DOMAIN_BENCHMARK,
    MAX_SCORE,
    ROLE_MAP,
)


# ---------------------------------------------------------------------------
# Text Extraction
# ---------------------------------------------------------------------------
def extract_text(uploaded_file) -> str:
    """Detect file type and extract raw text from the uploaded resume."""
    filename = uploaded_file.name.lower()

    if filename.endswith(".pdf"):
        return _extract_from_pdf(uploaded_file)
    elif filename.endswith(".docx"):
        return _extract_from_docx(uploaded_file)
    elif filename.endswith(".txt"):
        return _extract_from_txt(uploaded_file)
    else:
        raise ValueError(
            "Unsupported file format. Please upload a PDF, DOCX, or TXT file."
        )


def _extract_from_pdf(file) -> str:
    """Extract text from a PDF file using PyPDF2."""
    reader = PyPDF2.PdfReader(file)
    pages = [page.extract_text() or "" for page in reader.pages]
    return "\n".join(pages)


def _extract_from_docx(file) -> str:
    """Extract text from a DOCX file using python-docx."""
    doc = docx.Document(file)
    return "\n".join(paragraph.text for paragraph in doc.paragraphs)


def _extract_from_txt(file) -> str:
    """Read plain-text file content."""
    return file.read().decode("utf-8", errors="ignore")


# ---------------------------------------------------------------------------
# Text Preprocessing
# ---------------------------------------------------------------------------
def preprocess_text(raw_text: str) -> str:
    """Clean and normalize resume text for skill matching."""
    text = raw_text.lower()
    text = re.sub(r"[^a-z0-9\s\+\.\/#\-]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


# ---------------------------------------------------------------------------
# Skill Extraction
# ---------------------------------------------------------------------------
def extract_skills(cleaned_text: str) -> dict[str, list[str]]:
    """
    Match skills from the resume text against the skills dictionary.

    Returns a dict mapping each domain to its list of detected skills.
    """
    detected: dict[str, list[str]] = {}

    for domain, skills in SKILLS_DB.items():
        matched: list[str] = []
        seen_display: set[str] = set()
        for skill in skills:
            pattern = re.escape(skill)
            regex = rf"(?<![a-z]){pattern}(?![a-z+])"
            if re.search(regex, cleaned_text):
                display = DISPLAY_NAME_OVERRIDES.get(skill, skill.title())
                if display not in seen_display:
                    matched.append(display)
                    seen_display.add(display)
        if matched:
            detected[domain] = matched

    return detected


def count_skill_frequencies(
    cleaned_text: str, detected_skills: dict[str, list[str]]
) -> Counter:
    """Count how many times each detected skill appears in the resume."""
    freq: Counter = Counter()
    for skills in detected_skills.values():
        for skill in skills:
            pattern = re.escape(skill.lower())
            freq[skill] = len(re.findall(pattern, cleaned_text))
    return freq


# ---------------------------------------------------------------------------
# Resume Scoring
# ---------------------------------------------------------------------------
def calculate_strength_score(detected_skills: dict[str, list[str]]) -> float:
    """
    Calculate a resume strength percentage.

    Uses realistic benchmarks; hard-capped at MAX_SCORE.
    """
    total_detected = sum(len(v) for v in detected_skills.values())
    domains_covered = len(detected_skills)

    skill_score = min(total_detected / SKILL_BENCHMARK, 1.0)
    domain_score = min(domains_covered / DOMAIN_BENCHMARK, 1.0)

    depth_bonus = 0.0
    for skills in detected_skills.values():
        if len(skills) >= 5:
            depth_bonus = 1.0
            break
        elif len(skills) >= 3:
            depth_bonus = max(depth_bonus, 0.6)

    raw = (0.50 * skill_score + 0.30 * domain_score + 0.20 * depth_bonus) * 100
    score = raw * (MAX_SCORE / 100.0)
    return round(min(score, MAX_SCORE), 1)


# ---------------------------------------------------------------------------
# Job Role Recommendation
# ---------------------------------------------------------------------------
def recommend_role(detected_skills: dict[str, list[str]]) -> dict:
    """Recommend a primary job role and alternatives based on dominant domains."""
    if not detected_skills:
        return {
            "primary": "Unable to determine – not enough skills detected",
            "alternatives": [],
            "dominant_domain": "N/A",
        }

    domain_counts = {d: len(s) for d, s in detected_skills.items()}
    sorted_domains = sorted(domain_counts, key=domain_counts.get, reverse=True)
    dominant = sorted_domains[0]

    # Mixed-technical profile check
    if len(sorted_domains) >= 2:
        diff = domain_counts[sorted_domains[0]] - domain_counts[sorted_domains[1]]
        if diff <= 1:
            return {
                "primary": "Software Engineer",
                "alternatives": [
                    ROLE_MAP.get(sorted_domains[0], {}).get("primary", "Software Engineer"),
                    ROLE_MAP.get(sorted_domains[1], {}).get("primary", "Software Engineer"),
                ],
                "dominant_domain": "Mixed Technical",
            }

    entry = ROLE_MAP.get(dominant, {"primary": "Software Engineer", "alternatives": []})
    return {
        "primary": entry["primary"],
        "alternatives": entry["alternatives"],
        "dominant_domain": dominant,
    }
