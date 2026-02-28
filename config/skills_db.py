"""
config — Skills database and application constants.
"""

# ---------------------------------------------------------------------------
# Skills Dictionary – grouped by domain
# ---------------------------------------------------------------------------
SKILLS_DB: dict[str, list[str]] = {
    "Programming": [
        "python", "java", "c++", "javascript", "c language", "c programming",
        "typescript", "go", "rust", "ruby", "php", "swift", "kotlin",
        "scala", "r programming",
    ],
    "Web Development": [
        "react", "angular", "html", "css", "node.js", "vue.js", "django",
        "flask", "express.js", "next.js", "tailwind", "bootstrap",
        "rest api", "graphql",
    ],
    "Machine Learning / AI": [
        "machine learning", "deep learning", "tensorflow", "pytorch",
        "scikit-learn", "keras", "nlp", "natural language processing",
        "computer vision", "opencv", "transformers", "llm",
        "neural network", "reinforcement learning",
    ],
    "Data Science": [
        "sql", "postgresql", "pandas", "numpy", "data analysis",
        "power bi", "tableau", "matplotlib", "seaborn", "spark",
        "hadoop", "etl", "data visualization", "statistics",
        "excel", "mongodb", "mysql",
    ],
    "Cloud & DevOps": [
        "aws", "azure", "gcp", "docker", "kubernetes", "terraform",
        "ci/cd", "jenkins", "ansible", "cloudformation", "lambda",
        "s3", "ec2",
    ],
    "Tools": [
        "git", "linux", "github", "gitlab", "jira", "confluence",
        "vs code", "postman", "bash", "shell scripting",
    ],
}

# Display-name overrides for multi-word search terms
DISPLAY_NAME_OVERRIDES: dict[str, str] = {
    "c language": "C",
    "c programming": "C",
    "r programming": "R",
}

# Scoring constants
SKILL_BENCHMARK = 12       # skills needed for full skill-count score
DOMAIN_BENCHMARK = 3        # domains needed for full breadth score
MAX_SCORE = 92.0            # hard cap — no resume is "perfect"

# Role mapping
ROLE_MAP: dict[str, dict] = {
    "Machine Learning / AI": {
        "primary": "Machine Learning Engineer",
        "alternatives": ["AI Research Scientist", "NLP Engineer", "Data Scientist"],
    },
    "Web Development": {
        "primary": "Frontend / Full Stack Developer",
        "alternatives": ["UI Engineer", "Web Developer", "React Developer"],
    },
    "Data Science": {
        "primary": "Data Analyst / Data Scientist",
        "alternatives": [
            "Business Intelligence Analyst",
            "Analytics Engineer",
            "Database Developer",
        ],
    },
    "Cloud & DevOps": {
        "primary": "Cloud Engineer",
        "alternatives": [
            "DevOps Engineer",
            "Site Reliability Engineer",
            "Infrastructure Engineer",
        ],
    },
    "Programming": {
        "primary": "Machine Learning Engineer",
        "alternatives": [
            "Backend Developer",
            "Systems Programmer",
            "Application Developer",
        ],
    },
    "Tools": {
        "primary": "Software Engineer/ML Engineer",
        "alternatives": ["DevOps Engineer", "Systems Administrator"],
    },
}
