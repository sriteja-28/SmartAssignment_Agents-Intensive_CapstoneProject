# Smart Assignment Helper

Fast PDF reading, focused answers, and study memory for students.

## Features
- Multi-agent pipeline: ingest, index, summarize, answer, memory
- FAISS-backed vector store (optional) with TF-IDF fallback
- Optional OpenAI integration via `OPENAI_API_KEY`
- CLI demo and basic tests
- SQLite memory bank
- GitHub Actions CI workflow

## Quickstart
1. Create venv and activate:
```bash
python -m venv venv
source venv/bin/activate  # windows: venv\Scripts\activate
