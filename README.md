# obsidian-rag

A question-answering system over my Obsidian lecture notes. You ask a question, it retrieves the relevant notes, and a local model answers from them with citations. Runs fully locally, no API keys.

Stack: Postgres + pgvector, sentence-transformers for embeddings, BM25 for keyword search, Ollama (llama3.2) for generation, Docker for Postgres.

## How it works

Indexing (`ingest.py`, `embed.py`, `db.py`): split each note into chunks, embed them, store the chunks and vectors in Postgres.

Answering (`ask.py`, `answer.py`): hybrid search (vector plus BM25, fused with reciprocal rank fusion) picks the top notes, then the local model answers from their full text.

## Retrieval eval

Most of the work went into measuring retrieval, not the generation. `eval.py` runs 51 hand-labelled questions and reports recall@3: how often the correct note is in the top three results. The questions are varied on purpose: paraphrased, indirect, rare exact terms, and cross-language.

The score drove the changes (full log in NOTES.md). Some important ones:

- Chunking. Long notes were stored as one chunk, and the embedding model only reads about the first 128 tokens, so most of a long note was never embedded. Splitting them fixed several misses and got pure vector search to 0.78.
- Hybrid search. Adding BM25 made it worse at first (0.55), then roughly matched vector search once I fixed the tokenizer (0.73). It only beat vector as a lightly weighted tie-breaker for rare exact terms (0.82 at a 0.05 keyword weight).

Limits: 51 questions is small and the weight was tuned on it, so 0.82 is optimistic. Answers are short because the model is small.

## Running it

Needs Docker, Python, and Ollama.

```
docker compose up -d          # starts Postgres, loads the schema on first run
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
ollama pull llama3.2:1b
```

Copy `.env.example` to `.env` and set your vault path and database URL. Then:

```
python db.py                             # index the notes
python answer.py "what is an AVL tree"   # ask
python eval.py                           # retrieval score
```
