from pathlib import Path
from math import sqrt
import re

def tokenize(text: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", text.lower())

def chunk_text(text: str, chunk_size: int = 80) -> list[str]:
    words = text.split()
    return [" ".join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]

def vectorize(text: str) -> dict[str, int]:
    v = {}
    for token in tokenize(text):
        v[token] = v.get(token, 0) + 1
    return v

def cosine(a: dict[str, int], b: dict[str, int]) -> float:
    if not a or not b:
        return 0.0
    dot = sum(a.get(k, 0) * v for k, v in b.items())
    na = sqrt(sum(v*v for v in a.values()))
    nb = sqrt(sum(v*v for v in b.values()))
    return dot / (na * nb) if na and nb else 0.0

def build_index(folder: str) -> list[dict]:
    records = []
    for path in sorted(Path(folder).glob("*.txt")):
        text = path.read_text(encoding="utf-8")
        for i, chunk in enumerate(chunk_text(text)):
            records.append({"source": path.name, "chunk_id": i, "text": chunk, "vector": vectorize(chunk)})
    return records

def search(index: list[dict], query: str, top_k: int = 3) -> list[dict]:
    qv = vectorize(query)
    ranked = [{**item, "score": cosine(qv, item["vector"])} for item in index]
    return sorted(ranked, key=lambda x: x["score"], reverse=True)[:top_k]
