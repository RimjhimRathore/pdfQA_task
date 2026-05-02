import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class Retriever:
    def __init__(self):
        self.chunks = []
        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.matrix = None

    def index(self, chunks: list):
        """Build TF-IDF matrix from all text chunks."""
        self.chunks = chunks
        self.matrix = self.vectorizer.fit_transform(chunks)
        print(f"✅ Indexed {len(chunks)} chunks.")

    def get_top_chunks(self, question: str, top_k: int = 3) -> list:
        """
        Convert question to TF-IDF vector,
        then find top-k most similar chunks using cosine similarity.
        """
        q_vec = self.vectorizer.transform([question])
        scores = cosine_similarity(q_vec, self.matrix).flatten()
        top_indices = np.argsort(scores)[::-1][:top_k]
        # Only return chunks with non-zero similarity score
        return [self.chunks[i] for i in top_indices if scores[i] > 0]