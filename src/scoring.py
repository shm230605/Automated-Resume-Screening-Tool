# src/scoring.py

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_similarity(job_desc, resumes):
    """
    Calculate cosine similarity between job description and resumes
    """

    # Combine all documents
    documents = [job_desc] + resumes

    # Convert text to TF-IDF vectors
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(documents)

    # Compute cosine similarity
    similarity_scores = cosine_similarity(vectors[0:1], vectors[1:])

    return similarity_scores[0]