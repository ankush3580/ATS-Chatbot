def calculate_ats_score(similarity_score, matching_skills, jd_skills):
    """
    Calculate an overall ATS score.

    Weighting:
        - 60% skill matching
        - 40% TF-IDF similarity

    Args:
        similarity_score (float): TF-IDF cosine similarity (0 to 1).
        matching_skills (list): Skills found in both resume and JD.
        jd_skills (list): Skills required by the JD.

    Returns:
        float: ATS score from 0 to 100.
    """

    if len(jd_skills) == 0:
        skill_score = 0
    else:
        skill_score = len(matching_skills) / len(jd_skills)

    ats_score = (
        (skill_score * 0.60) +
        (similarity_score * 0.40)
    ) * 100

    return round(ats_score, 2)


if __name__ == "__main__":
    similarity = 0.5359

    matching_skills = [
        "machine learning",
        "python",
        "scikit-learn",
        "sql"
    ]

    jd_skills = [
        "data visualization",
        "machine learning",
        "numpy",
        "pandas",
        "python",
        "scikit-learn",
        "sql",
        "statistics"
    ]

    score = calculate_ats_score(
        similarity,
        matching_skills,
        jd_skills
    )

    print("ATS Score:")
    print(f"{score}%")