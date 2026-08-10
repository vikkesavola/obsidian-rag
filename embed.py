from sentence_transformers import SentenceTransformer
from ingest import load_chunks
from config import EMBED_MODEL

model = SentenceTransformer(EMBED_MODEL)

def get_embeddings():
  chunks = load_chunks()
  texts = [c["text"] for c in chunks]
  embeddings = model.encode(texts, show_progress_bar=True)

  for chunk, vec in zip(chunks, embeddings):
    chunk["embedding"] = vec

  return chunks