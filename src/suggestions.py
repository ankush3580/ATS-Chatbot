def generate_suggestions(missing_skills, similarity_score, ats_score):
    """
    Generate resume improvement suggestions based on ATS analysis.

    Args:
        missing_skills (list): Skills present in the JD but missing from resume.
        similarity_score (float): TF-IDF similarity score from 0 to 1.
        ats_score (float): Overall ATS score from 0 to 100.

    Returns:
        list: Resume improvement suggestions.
    """

    suggestions = []

    if missing_skills:
        skills_text = ", ".join(missing_skills)

        suggestions.append(
            f"Consider adding relevant experience or projects involving: {skills_text}, "
            "if you genuinely have those skills."
        )

    if similarity_score < 0.40:
        suggestions.append(
            "The resume has relatively low textual similarity with the job description. "
            "Consider tailoring your project and experience descriptions to the role."
        )
    elif similarity_score < 0.70:
        suggestions.append(
            "The resume has moderate similarity with the job description. "
            "Consider using more relevant terminology from the job description where accurate."
        )
    else:
        suggestions.append(
            "The resume has strong textual similarity with the job description."
        )

    if ats_score < 50:
        suggestions.append(
            "Consider improving alignment between the resume and the job requirements."
        )
    elif ats_score < 70:
        suggestions.append(
            "The resume has moderate alignment with the job requirements. "
            "Addressing missing skills may improve the score."
        )
    else:
        suggestions.append(
            "The resume shows strong alignment with the analyzed job description."
        )

    return suggestions


if __name__ == "__main__":
    missing_skills = [
        "data visualization",
        "numpy",
        "pandas",
        "statistics"
    ]

    similarity_score = 0.5359
    ats_score = 51.44

    suggestions = generate_suggestions(
        missing_skills,
        similarity_score,
        ats_score
    )

    print("Resume Improvement Suggestions:")

    for i, suggestion in enumerate(suggestions, start=1):
        print(f"{i}. {suggestion}")