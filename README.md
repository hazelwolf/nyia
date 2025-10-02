# Not Your Idiotic Assistant

A futuristic assistant leveraging the latest GenAI technologies and tools to adapt and augment human intelligence. **NYIA** combines state-of-the-art language models, retrieval-augmented generation (RAG), semantic kernels, and modern frameworks to deliver intelligent, context-aware assistance for a wide range of tasks.

## Features

- **GenAI-Powered**: Integrates advanced LLMs via [Ollama](https://github.com/ollama/ollama-python) and [Langchain](https://www.langchain.com/).
- **FastAPI Backend**: High-performance Python API for extensibility and integration.
- **Configurable Models**: Easily switch and configure LLMs using environment variables.
- **Modular Architecture**: Organized codebase for agents, core logic, and frameworks.
- **MCP (Multi-Component Pipeline)**: Flexible orchestration of multiple AI components for complex workflows.
- **Tool Integration**: Extensible tools for search, data processing, and automation.
- **Retrieval-Augmented Generation (RAG)**: Enhanced responses using external knowledge sources and document retrieval.
- **Semantic Kernels**: Advanced context management and reasoning for improved task execution.
- **Cutting-Edge GenAI Tech**: Rapid adoption of emerging AI frameworks and best practices.

## Getting Started

1. **Clone the repository**
   ```sh
   git clone https://github.com/hazelwolf/nyia
   cd nyia
   ```

2. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```
   Or use [uv](https://docs.astral.sh/uv/) for faster installs.

3. **Configure environment**
   - Copy `.env.example` to `.env` and set your model preferences.

4. **Run the assistant**
   ```sh
   python main.py
   ```
   (or)
    ```sh
   uv run main.py
   ```

## Project Structure

```
.
├── main.py
├── src/
│   ├── agents/
│   ├── core/
│   ├── frameworks/
│   │   └── ollama_llm.py
│   ├── mcp/
│   └── tools/
├── .env
├── pyproject.toml
├── README.md
└── docs/
```

## References

Find all the OSS and third party code and software used [here](/docs/).

---

> NYIA: Not Your Idiotic Assistant – Augmenting human intelligence with the latest GenAI stack.