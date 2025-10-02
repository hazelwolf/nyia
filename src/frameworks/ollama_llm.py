from ollama import chat
from ollama import ChatResponse
from dotenv import load_dotenv
import os

load_dotenv()
llm_model = os.getenv('ollama_model')

def OllamaChat(prompt: str) -> ChatResponse:
  response: ChatResponse = chat(model=llm_model, messages=[
    {
      'role': 'user',
      'content': prompt,
    },
  ])
  return response

def OllamaChatStream(prompt: str) -> ChatResponse:
  response: ChatResponse = chat(model=llm_model, messages=[
    {
      'role': 'user',
      'content': prompt,
    },
  ], stream=True)
  return response