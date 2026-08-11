import sys
import psycopg
from pgvector.psycopg import register_vector
from config import EMBED_MODEL, DATABASE_URL
from sentence_transformers import SentenceTransformer

model = SentenceTransformer(EMBED_MODEL)

def search(question, k=5):
  question_embed = model.encode(question)

  with psycopg.connect(DATABASE_URL) as conn:
    register_vector(conn)
    with conn.cursor() as cur:
      cur.execute("""SELECT d.doc_name, c.chunk->>'text' 
        FROM document_chunks c
        JOIN documents d
        ON c.document_id = d.id
        ORDER BY c.embedding <=> %s
        LIMIT %s
      """, (question_embed, k))
  
      return cur.fetchall()

if __name__ == "__main__":
  question = " ".join(sys.argv[1:])
  for doc_name, text in search(question):
    print(f"{doc_name}\n{text[:150]}\n")