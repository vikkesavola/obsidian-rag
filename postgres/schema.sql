-- Enable pgvector extension
CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE documents (
  id bigserial PRIMARY KEY, 
  doc_name varchar(256),
  created_at timestamp default now()
);

CREATE TABLE document_chunks (
  id bigserial PRIMARY KEY,                             -- chunk's own id
  document_id bigint not null references documents(id), -- which doc it belongs to
  chunk jsonb,
  embedding vector(1536),
  created_at timestamp default now()
);


