from typing import List
from sentence_transformers import SentenceTransformer

class DocumentEmbedder:
    def __init__(self, model_name="sentence-transformers/all-MiniLM-L6-v2"):
        print(f"Loading embedding model: {model_name}")
        self.model = SentenceTransformer(model_name)

    def encode_docs(self, docs: List[dict], batch_size = 64):
        print("Embedding documents...")

        texts = [doc["text"] for doc in docs]

        embeddings = self.model.encode(
            texts,
            batch_size=batch_size,
            show_progress_bar=True,
            convert_to_tensor=False,   # return numpy for FAISS
            normalize_embeddings=True  # cosine similarity embeddings
        )
        return embeddings

    def encode_query(self, query: str):
        return self.model.encode(
            [query],
            convert_to_tensor=False,
            normalize_embeddings=True
        ).astype("float32")

