import os
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss
import ollama

class LocalRAG:
    def __init__(self, docs_path="docs", similarity_threshold=0.6):
        self.docs_path = docs_path
        self.similarity_threshold = similarity_threshold
        self.embedder = SentenceTransformer("all-MiniLM-L6-v2")
        self.docs, self.doc_texts = self.load_docs()
        self.index, self.embeddings = self.build_index()

    def load_docs(self):
        docs = []
        for filename in os.listdir(self.docs_path):
            if filename.endswith(".txt"):
                path = os.path.join(self.docs_path, filename)
                with open(path, "r", encoding="utf-8") as f:
                    docs.append(f.read())
        return docs, docs

    def build_index(self):
        embeddings = self.embedder.encode(self.doc_texts)
        dim = embeddings.shape[1]
        index = faiss.IndexFlatL2(dim)
        index.add(np.array(embeddings))
        return index, embeddings

    def retrieve(self, query, top_k=2):
        query_embedding = self.embedder.encode([query])
        distances, indices = self.index.search(query_embedding, top_k)
        context_docs = []
        for idx, distance in zip(indices[0], distances[0]):
            if distance < self.similarity_threshold:
                context_docs.append(self.doc_texts[idx])
        return context_docs

    def query_rag(self, query):
        context_docs = self.retrieve(query)
        if context_docs:
            context = "\n\n".join(context_docs)
            return f"Here's what I found:\n{context}"
        else:
            return None


rag = LocalRAG()

def query_rag(query):
    response = rag.query_rag(query)
    if response:
        return response
    else:
        # Fallback to local Ollama for out of the context questions
        result = ollama.chat(model="llama3", messages=[{"role": "user", "content": query}])
        return result['message']['content']
