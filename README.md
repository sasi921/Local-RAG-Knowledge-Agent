# Local RAG Knowledge Agent

A lightweight, fully local **Retrieval-Augmented Generation (RAG) knowledge agent** that searches text documents, ranks relevant chunks, and returns grounded answers with citations.

## Architecture

`Question → tokenize → vectorize → cosine similarity → top-k retrieval → grounded answer + citations`

## Features

- Local `.txt` knowledge base
- Automatic chunking
- Lightweight bag-of-words vectors
- Cosine-similarity retrieval
- Top-k ranking
- Citation generation
- No API key required
- Deterministic and easy to test
- 4 automated tests

## Run

```bash
python app.py "How are production releases handled?"
python app.py "How does the AI team ground answers?"
pytest -q
```

## What to learn

RAG fundamentals, chunking, retrieval, similarity scoring, grounded generation patterns, citations, and hallucination resistance.

## Next upgrades

Embeddings, vector database, PDF ingestion, hybrid search, LLM synthesis, and evaluation metrics.

## AI Agent Engineering Lab

This is a standalone project in the AI Agent Engineering Lab portfolio.
