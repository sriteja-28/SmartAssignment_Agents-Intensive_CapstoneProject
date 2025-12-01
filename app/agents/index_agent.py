from app.tools.embedding_store import EmbeddingStoreFactory

class IndexAgent:
    def __init__(self):
        self.store = EmbeddingStoreFactory.get_store()

    def index_document(self, doc):
        chunks = []
        for i, page in enumerate(doc['pages']):
            chunk = {
                'doc_id': doc['id'],
                'chunk_id': f"{doc['id']}_p{i}",
                'text': page,
                'meta': {'page': i+1, 'title': doc['title']}
            }
            chunks.append(chunk)
        self.store.add_chunks(chunks)

    def retrieve(self, query, top_k=5):
        return self.store.query(query, top_k=top_k)
