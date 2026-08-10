from dotenv import load_dotenv
from openai import OpenAI
from ingest import load_chunks
from config import EMBED_MODEL

load_dotenv()
client = OpenAI()

response = client.embeddings.create(
    input=load_chunks(), model=EMBED_MODEL
)

print(response.data[0].embedding)