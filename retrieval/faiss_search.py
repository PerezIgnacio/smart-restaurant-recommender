import faiss

class FaissIndex:
    def __init__(self, dim):
        self.dim = dim
        self.index = faiss.IndexFlatIP(dim)
        self.docs = []
        self.docs_ids = []

    def add(self, embeddings, docs, docs_ids):
        self.docs.extend(docs)
        self.docs_ids.extend(docs_ids)
        self.index.add(embeddings)

    def search(self, query_embedding, k=50):
        scores, idxs = self.index.search(query_embedding, k)

        results = []
        for score, i in zip(scores[0], idxs[0]):
            results.append({
                "doc_id": self.docs_ids[i],
                "score": float(score),
                "text": self.docs[i]['text'],
            })

        return results[:k]

    def size(self):
        return self.index.ntotal
