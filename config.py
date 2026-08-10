import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

VAULT_PATH   = Path(os.environ["VAULT_PATH"])
DATABASE_URL = os.environ["DATABASE_URL"]
EMBED_MODEL  = "text-embedding-3-small"
EMBED_DIM    = 1536