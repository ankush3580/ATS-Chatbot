import re


TECHNICAL_SKILLS = {
    "python",
    "java",
    "c",
    "c++",
    "c#",
    "sql",
    "mysql",
    "postgresql",
    "mongodb",
    "html",
    "css",
    "javascript",
    "typescript",
    "react",
    "node.js",
    "flask",
    "django",
    "fastapi",
    "pandas",
    "numpy",
    "scikit-learn",
    "tensorflow",
    "pytorch",
    "keras",
    "opencv",
    "machine learning",
    "deep learning",
    "natural language processing",
    "nlp",
    "computer vision",
    "data science",
    "data analytics",
    "data visualization",
    "statistics",
    "matplotlib",
    "seaborn",
    "git",
    "github",
    "docker",
    "linux",
    "aws",
    "azure",
    "gcp",
    "kubernetes",
    "rest api",
    "api",
    "excel",
    "power bi",
    "tableau",
}


def skill_found(skill, text):
    """
    Check whether a skill appears as a separate term
    instead of merely appearing as a substring.
    """

    pattern = r"(?<![a-z0-9+#])" + re.escape(skill) + r"(?![a-z0-9+#])"

    return re.search(pattern, text, re.IGNORECASE) is not None


def extract_skills(text):
    """
    Extract known technical skills from text.

    Args:
        text (str): Resume or job-description text.

    Returns:
        list: Technical skills found in the text.
    """

    found_skills = []

    for skill in TECHNICAL_SKILLS:
        if skill_found(skill, text):
            found_skills.append(skill)

    return sorted(found_skills)


def compare_skills(resume_text, jd_text):
    """
    Compare skills between a resume and job description.

    Returns:
        dict: Matching and missing skills.
    """

    resume_skills = set(extract_skills(resume_text))
    jd_skills = set(extract_skills(jd_text))

    matching_skills = resume_skills.intersection(jd_skills)
    missing_skills = jd_skills.difference(resume_skills)

    return {
        "resume_skills": sorted(resume_skills),
        "jd_skills": sorted(jd_skills),
        "matching_skills": sorted(matching_skills),
        "missing_skills": sorted(missing_skills),
    }


if __name__ == "__main__":
    resume = """
    Python, C++, Machine Learning, SQL, Flask, Scikit-learn
    """

    jd = """
    Python, SQL, Machine Learning, Pandas, NumPy,
    Scikit-learn, Statistics, Data Visualization
    """

    result = compare_skills(resume, jd)

    print("Resume Skills:")
    print(result["resume_skills"])

    print("\nJD Skills:")
    print(result["jd_skills"])

    print("\nMatching Skills:")
    print(result["matching_skills"])

    print("\nMissing Skills:")
    print(result["missing_skills"])