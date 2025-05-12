from fastapi import FastAPI
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

app = FastAPI()
model = SentenceTransformer('all-MiniLM-L6-v2')
docs = ["TSMC earnings report shows strong growth", "Samsung earnings dipped slightly"]
embeddings = model.encode(docs)
index = faiss.IndexFlatL2(384)
index.add(np.array(embeddings))

@app.get("/retrieve")
def retrieve(query: str):
    query_embedding = model.encode([query])
    D, I = index.search(np.array(query_embedding), k=1)
    return {"result": docs[I[0][0]]}
