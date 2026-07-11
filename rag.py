from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

def create_vector_store(text):
    chunks = [text[i:i+500] for i in range(0, len(text), 500)]

    embeddings = model.encode(chunks)

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings))

    return index, chunks


def search(index, chunks, query):
    query_embedding = model.encode([query])

    _, indices = index.search(np.array(query_embedding), k=3)

    return [chunks[i] for i in indices[0]]
