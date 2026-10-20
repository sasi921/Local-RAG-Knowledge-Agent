import argparse, json
from agent import answer_question

def main():
    p = argparse.ArgumentParser(description="Local RAG Knowledge Agent")
    p.add_argument("question")
    p.add_argument("--docs", default="examples")
    p.add_argument("--top-k", type=int, default=3)
    args = p.parse_args()
    print(json.dumps(answer_question(args.docs, args.question, args.top_k), indent=2))

if __name__ == "__main__":
    main()
