from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_similarity(resume_text, jd_text):
    """
    Calculate similarity between a resume and a job description
    using TF-IDF and cosine similarity.

    Args:
        resume_text (str): Resume text.
        jd_text (str): Job description text.

    Returns:
        float: Similarity score between 0 and 1.
    """

    documents = [resume_text, jd_text]

    vectorizer = TfidfVectorizer(stop_words="english")

    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity_matrix = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])

    return float(similarity_matrix[0][0])


if __name__ == "__main__":
    resume = """
    Python, C++, Machine Learning, SQL, Flask, Scikit-learn.
    Experience with building machine learning applications.
    """

    jd = """
    Looking for a Data Science Intern with Python, SQL,
    Machine Learning and Scikit-learn experience.
    """

    score = calculate_similarity(resume, jd)

    print("TF-IDF Cosine Similarity:")
    print(round(score, 4))

    print("Similarity Percentage:")
    print(round(score * 100, 2), "%")