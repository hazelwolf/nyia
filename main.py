from src.frameworks.ollama_llm import OllamaChatStream


def main():
    print("Hello from nyia!")
    response = OllamaChatStream("Why is the sky blue?")
    for chunk in response:
        print(chunk['message']['content'], end='', flush=True)
    print()  # for newline after the stream ends

if __name__ == "__main__":
    main()
