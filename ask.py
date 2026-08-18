import sys
import psycopg
from pgvector.psycopg import register_vector
from config import EMBED_MODEL, DATABASE_URL
from sentence_transformers import SentenceTransformer
from rank_bm25 import BM25Okapi
import re

model = SentenceTransformer(EMBED_MODEL)

def _tokenize(text):
  return re.findall(r"\w+", text.lower())

def _load_corpus():
  with psycopg.connect(DATABASE_URL) as conn, conn.cursor() as cur:
    cur.execute("SELECT d.doc_name, c.chunk->>'text' "
                "FROM document_chunks c JOIN documents d ON c.document_id = d.id")
    rows = cur.fetchall()
  docs = [name for name, _ in rows]
  corpus = [_tokenize(text) for _, text in rows]
  return docs, BM25Okapi(corpus)

DOCS, BM25 = _load_corpus()

def search_bm25(question, k=20):
  scores = BM25.get_scores(_tokenize(question))
  ranked = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)
  seen = []
  for i in ranked:
    if DOCS[i] not in seen:
      seen.append(DOCS[i])
    if len(seen) == k:
      break
  return seen

def search_semantic(question, k=5):
  question_embed = model.encode(question)

  with psycopg.connect(DATABASE_URL) as conn:
    register_vector(conn)
    with conn.cursor() as cur:
      cur.execute("""
        SELECT doc_name, text 
        FROM (
          SELECT DISTINCT ON (d.doc_name)
            d.doc_name, c.chunk->>'text' AS text, c.embedding <=> %s AS distance
          FROM document_chunks c JOIN documents d ON c.document_id = d.id
          ORDER BY d.doc_name, distance
        ) sub
        ORDER BY distance
        LIMIT %s
      """, (question_embed, k))
  
      return cur.fetchall()

def rrf(rankings, k=60):
  scores = {}
  for ranking, weight in rankings:
    for rank, name in enumerate(ranking):
      scores[name] = scores.get(name, 0) + weight * ( 1 / (k + rank))
  return sorted(scores, key=scores.get, reverse=True)

def search_hybrid(question, top_k=3, pool=20):
  vec = [name for name, _ in search_semantic(question, k=pool)]
  kw = search_bm25(question, k=pool)
  return rrf([(vec, 1), (kw, 0.00)])[:top_k]

if __name__ == "__main__":
  question = " ".join(sys.argv[1:])
  for name in search_hybrid(question):
    print(name)