from pathlib import Path
from config import VAULT_PATH

def load_chunks():
  chunks = []
  for md in VAULT_PATH.rglob('*.md'):
    text = md.read_text(encoding="utf-8")
    if text.startswith("---"):
      _, frontmatter, body = text.split("---", 2)
    else: frontmatter, body = "", text
    parts = body.split("\n## ") if len(body) > 1500 else [body]

    for part in parts:
      chunks.append({
        "note_path": str(md.relative_to(VAULT_PATH)),
        "text": part.strip()
      })

  return chunks