from config import EMBED_MODEL, DATABASE_URL
import psycopg
from psycopg.types.json import Json
from pgvector.psycopg import register_vector
from embed import get_embeddings


def store(chunks):
  with psycopg.connect(DATABASE_URL) as conn:
    register_vector(conn)
    with conn.cursor() as cur:
      doc_ids = {}
      for c in chunks:
        path = c["note_path"]
        if path not in doc_ids:
          cur.execute(
            "INSERT INTO documents (doc_name) VALUES (%s) RETURNING id",
            (c["note_path"],),
          )
          doc_ids[path] = cur.fetchone()[0]
        cur.execute(
          "INSERT INTO document_chunks (document_id, chunk, embedding) VALUES (%s, %s, %s)",
          (doc_ids[path], Json({"text": c["text"]}), c["embedding"]),
        )
    conn.commit()


if __name__ == "__main__":
    chunks = get_embeddings()
    store(chunks)
    print(f"indexed {len(chunks)} chunks")
