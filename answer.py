from ollama import chat
from ollama import ChatResponse

def getResponse(context, question):
  prompt = f"""Notes:
  {context}

  Question: {question}

  Answer in English, using only the notes above. If the notes do not contain the answer, say so instead of guessing. Cite the note(s) you used.
  """
  response: ChatResponse = chat(model='llama3.2:1b', messages=[
    {
      'role': 'user',
      'content': prompt,
    },
  ])

  return response.message.content


if __name__ == "__main__":
  import sys
  from config import VAULT_PATH
  from ask import search_hybrid

  question = " ".join(sys.argv[1:])
  notes = search_hybrid(question, top_k=3)
  context = "\n\n".join(
    f"### {p}\n{(VAULT_PATH / p).read_text(encoding='utf-8')}" for p in notes
  )
  print(getResponse(context, question))