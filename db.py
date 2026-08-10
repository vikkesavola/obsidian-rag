from openai import OpenAI
from ingest import load_chunks
from config import EMBED_MODEL, DATABASE_URL
import psycopg
from psycopg.types.json import Json
from pgvector.psycopg import register_vector

client = OpenAI()

def get_embeddings():
  chunks = load_chunks()
  texts = [c["text"] for c in chunks]

  response = client.embeddings.create(input=texts, model=EMBED_MODEL)

  for chunk, item in zip(chunks, response.data):
    chunk["embedding"] = item.embedding

  print(len(chunks), "chunks,", len(chunks[0]["embedding"]), "dims")



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
          "INSERT INTO document_chunks (document_id, chunk, embedding) VALUES (%s %s %s)",
          (doc_ids[path], Json({"text": c["text"]}), c["embedding"]),
        )
    conn.commit()
