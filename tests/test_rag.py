from pathlib import Path
from rag import vectorize, cosine, build_index, search
from agent import answer_question

def test_cosine_similarity():
    assert cosine(vectorize("rag retrieval"), vectorize("rag retrieval")) > 0.99

def test_index_and_search(tmp_path: Path):
    (tmp_path/"a.txt").write_text("Kubernetes runs containerized workloads.")
    (tmp_path/"b.txt").write_text("RAG retrieves relevant document chunks.")
    idx = build_index(str(tmp_path))
    results = search(idx, "document retrieval")
    assert results[0]["source"] == "b.txt"

def test_grounded_answer(tmp_path: Path):
    (tmp_path/"notes.txt").write_text("Production releases require automated tests and CI CD.")
    result = answer_question(str(tmp_path), "What is required for production releases?")
    assert result["citations"]
    assert "automated tests" in result["answer"]

def test_no_evidence(tmp_path: Path):
    (tmp_path/"notes.txt").write_text("Kubernetes runs containers.")
    result = answer_question(str(tmp_path), "What is the vacation policy?")
    assert result["citations"] == []
