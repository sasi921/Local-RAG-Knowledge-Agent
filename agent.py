from rag import build_index, search

def answer_question(folder: str, question: str, top_k: int = 3) -> dict:
    index = build_index(folder)
    if not index:
        return {"answer": "No knowledge files found.", "citations": [], "matches": []}
    matches = [m for m in search(index, question, top_k) if m["score"] > 0]
    if not matches:
        return {"answer": "I could not find grounded evidence for that question.", "citations": [], "matches": []}
    evidence = " ".join(m["text"] for m in matches)
    citations = [f"{m['source']}#chunk-{m['chunk_id']}" for m in matches]
    return {"answer": evidence, "citations": citations, "matches": [{"source": m["source"], "chunk_id": m["chunk_id"], "score": round(m["score"], 4)} for m in matches]}
