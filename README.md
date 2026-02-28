# AI Resume Analyzer

A Streamlit-based web application that analyzes resumes, extracts technical skills, calculates a strength score, and recommends suitable job roles.

---

## Project Structure

```
Resume_skill_analyzer/
│
├── app.py                  # Streamlit entry point (UI layout)
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── .gitignore              # Git ignore rules
│
├── config/                 # Configuration & constants
│   ├── __init__.py
│   └── skills_db.py        # Skills dictionary, role map, scoring constants
│
├── styles/                 # UI styling
│   ├── __init__.py
│   └── theme.py            # Dark & light theme CSS, chart color palettes
│
└── utils/                  # Core logic
    ├── __init__.py
    ├── analyzer.py          # Text extraction, preprocessing, skill matching, scoring, role recommendation
    └── charts.py            # Theme-aware Plotly chart builders (pie chart, bar chart)
```

---

## Features

- **Resume Upload** — supports PDF, DOCX, and TXT formats
- **Text Extraction** — PyPDF2 for PDF, python-docx for DOCX, direct read for TXT
- **Preprocessing** — lowercase, remove punctuation/special characters/extra spaces
- **Skill Detection** — regex-based matching against 70+ skills across 6 domains
- **Strength Scoring** — weighted formula (skill count + domain breadth + depth bonus), capped at 92%
- **Role Recommendation** — intelligent mapping based on dominant skill domains
- **Analytics** — interactive Plotly donut chart and horizontal bar chart
- **Dark / Light Theme** — toggle between dark and light mode via the ☀️ switch; custom CSS and chart colors adapt automatically

---

## Skill Domains

| Domain              | Example Skills                                      |
|---------------------|-----------------------------------------------------|
| Programming         | Python, Java, C++, JavaScript, TypeScript, Go       |
| Web Development     | React, Angular, HTML, CSS, Node.js, Django           |
| Machine Learning/AI | TensorFlow, PyTorch, Scikit-learn, NLP, Deep Learning|
| Data Science        | SQL, Pandas, NumPy, Tableau, Power BI, Spark         |
| Cloud & DevOps      | AWS, Azure, Docker, Kubernetes, Terraform            |
| Tools               | Git, Linux, GitHub, Jira, Postman, Bash              |

---

## Setup & Run

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd Resume_skill_analyzer
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`.

---

## Dependencies

| Package      | Purpose                        |
|--------------|--------------------------------|
| streamlit    | Web UI framework               |
| PyPDF2       | PDF text extraction            |
| python-docx  | DOCX text extraction           |
| plotly        | Interactive charts             |

---

## How It Works

1. **Upload** a resume (PDF / DOCX / TXT)
2. Text is **extracted** and **preprocessed**
3. Skills are **matched** against the skills database using regex
4. A **strength score** is calculated (0–92%)
5. A **job role** is recommended based on the dominant skill domain
6. Results are displayed in a scrollable dashboard with charts

---

## Scoring Logic

- **50%** — skill count (benchmark: 12 skills = full marks)
- **30%** — domain breadth (benchmark: 3 domains = full marks)
- **20%** — depth bonus (3+ skills in one domain)
- **Hard cap** at 92% — no resume scores 100%

---

## License

MIT
