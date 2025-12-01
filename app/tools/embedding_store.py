import os
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

try:
    import faiss
    FAISS_AVAILABLE = True
except ImportError:
    FAISS_AVAILABLE = False

class EmbeddingStoreFactory:
    @staticmethod
    def get_store():
        if FAISS_AVAILABLE:
            return FAISSStore()
        else:
            return TFIDFStore()

class FAISSStore:
    def __init__(self, dim=512):
        self.dim = dim
        self.text_chunks = []
        self.vecs = None
        self.index = faiss.IndexFlatL2(dim)

    def add_chunks(self, chunks):
        for c in chunks:
            emb = np.random.rand(self.dim).astype('float32')  # placeholder
            self.index.add(np.expand_dims(emb, 0))
            self.text_chunks.append(c)

    def query(self, query, top_k=5):
        q_emb = np.random.rand(self.dim).astype('float32')
        D, I = self.index.search(np.expand_dims(q_emb, 0), top_k)
        return [self.text_chunks[i] for i in I[0] if i < len(self.text_chunks)]

class TFIDFStore:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.text_chunks = []
        self.vec_matrix = None

    def add_chunks(self, chunks):
        texts = [c['text'] for c in chunks]
        self.text_chunks.extend(chunks)
        if self.text_chunks:
            self.vec_matrix = self.vectorizer.fit_transform([c['text'] for c in self.text_chunks])

    def query(self, query, top_k=5):
        if self.vec_matrix is None or len(self.text_chunks) == 0:
            return []
        q_vec = self.vectorizer.transform([query])
        from sklearn.metrics.pairwise import cosine_similarity
        scores = cosine_similarity(q_vec, self.vec_matrix)[0]
        idxs = scores.argsort()[::-1][:top_k]
        return [self.text_chunks[i] for i in idxs]
    

