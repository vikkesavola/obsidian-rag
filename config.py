import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

VAULT_PATH   = Path(os.environ["VAULT_PATH"])
DATABASE_URL = os.environ["DATABASE_URL"]
EMBED_MODEL  = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
EMBED_DIM    = 384