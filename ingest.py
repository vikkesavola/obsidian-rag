from pathlib import Path
from config import VAULT_PATH, CHUNK_TARGET_CHARS


def pieces(section):
  for para in section.split("\n\n"):
    if len(para) <= CHUNK_TARGET_CHARS:
      yield para
    else:
      yield from para.split("\n")

def load_chunks():
  """
  Read every note in the vault and split it into embedding-sized chunks.
  Splits on ## headings and packs paragraphs to CHUNK_TARGET_CHARS.
  Returns a list {"note_path": str, "text": str}.
  """
  chunks = []
  for md in VAULT_PATH.rglob('*.md'):
    text = md.read_text(encoding="utf-8")
    if text.startswith("---"):
      _, frontmatter, body = text.split("---", 2)
    else: frontmatter, body = "", text
    sections = body.split("\n## ") if len(body) > 1500 else [body]

    for section in sections:
      buffer = ""
      for para in pieces(section):
        if buffer and len(buffer) + len(para) > CHUNK_TARGET_CHARS:
          chunks.append({
            "note_path": str(md.relative_to(VAULT_PATH)),
            "text": buffer.strip()
          })
          buffer = para
        else:
          buffer += "\n\n" + para
      if buffer:
        chunks.append({
          "note_path": str(md.relative_to(VAULT_PATH)),
          "text": buffer.strip()
        })

  return chunks