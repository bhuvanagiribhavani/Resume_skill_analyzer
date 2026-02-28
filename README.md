# 🤖 AI Resume Skill Analyzer  

A Streamlit-based web application that analyzes resumes, extracts technical skills, calculates a strength score, and recommends suitable job roles based on detected expertise.

This project demonstrates practical applications of:
- NLP-based text processing  
- Regex-based skill extraction  
- Domain-based evaluation logic  
- Interactive data visualization with Plotly  
- Clean UI design with theme support  

---

## 🚀 Features

- Upload resumes in PDF / DOCX / TXT format  
- Automatic text extraction and preprocessing  
- Intelligent skill matching using regex patterns  
- Domain-wise skill categorization  
- Resume strength score calculation (0–92%)  
- Smart job role recommendation  
- Interactive Plotly charts (Pie & Bar)  
- Dark and Light theme support  

---

## 📂 Project Structure

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
│   └── skills_db.py        # Skills dictionary & role mapping
│
├── styles/                 # UI styling
│   ├── __init__.py
│   └── theme.py            # Dark & light theme CSS, chart color palettes
│
└── utils/                  # Core logic
    ├── __init__.py
    ├── analyzer.py         # Text extraction, preprocessing, skill matching & role recommendation
    └── charts.py           # Theme-aware Plotly chart builders
```

---

## 🧠 Skill Domains

| Domain | Example Skills |
|--------|----------------|
| Programming | Python, Java, C++, JavaScript, TypeScript, Go |
| Web Development | React, Angular, HTML, CSS, Node.js, Django |
| Machine Learning / AI | TensorFlow, PyTorch, Scikit-learn, NLP, Deep Learning |
| Data Science | SQL, Pandas, NumPy, Tableau, Power BI, Spark |
| Cloud & DevOps | AWS, Azure, Docker, Kubernetes, Terraform |
| Tools | Git, Linux, GitHub, Jira, Postman, Bash |

---

## ⚙️ Setup & Installation

### 1. Clone the Repository

```bash
git clone <https://github.com/bhuvanagiribhavani/Resume_skill_analyzer.git>
cd Resume_skill_analyzer
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
streamlit run app.py
```

The application will launch at:

```
http://localhost:8501
```

---

## 📦 Dependencies

| Package | Purpose |
|----------|----------|
| streamlit | Web UI framework |
| PyPDF2 | PDF text extraction |
| python-docx | DOCX text extraction |
| plotly | Interactive visualizations |

---

## 🔍 How It Works

1. Upload a resume (PDF / DOCX / TXT)  
2. Resume text is extracted and cleaned  
3. Skills are matched against a predefined skills database using regex  
4. The dominant skill domain is identified  
5. A suitable job role is recommended  
6. Results are displayed in an interactive dashboard with charts  

---

## 💡 Example Role Recommendations

- Machine Learning Engineer  
- Data Scientist  
- Full Stack Developer  
- DevOps Engineer  
- Data Analyst  

---

## 🎯 Learning Outcomes

This project helps in understanding:

- Resume parsing techniques  
- Regex-based pattern extraction  
- Skill-domain mapping  
- Interactive data visualization  
- Modular project architecture  
- Building production-ready Streamlit applications  

---

## 👩‍💻 Author

**Bhuvanagiri Bhavani**  
  
