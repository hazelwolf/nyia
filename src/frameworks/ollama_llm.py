from ollama import chat
from ollama import ChatResponse
from dotenv import load_dotenv
import os

load_dotenv()
llm_model = os.getenv('ollama_model')

response: ChatResponse = chat(model=llm_model, messages=[
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },
])
print(response['message']['content'])
# or access fields directly from the response object
print(response.message.content)