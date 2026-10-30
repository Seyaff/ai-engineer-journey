from dotenv import load_dotenv
from pinecone import Pinecone
from sentence_transformers import SentenceTransformer

load_dotenv()
index = Pinecone().Index("faq")
model = SentenceTransformer("all-MiniLM-L6-v2")
THRESHOLD = 0.30

tests = [
    ("How much is Botox?", "chunk-2"),
    ("What happens if I miss my appointment?", "chunk-10"),
    ("Who won the World Cup?", None),
]

def grade(expected, top_id, score):
    if expected is None:
        return score < THRESHOLD
    return score >= THRESHOLD and top_id == expected

results = []
for question, expected in tests:
    q_vec = model.encode(question, normalize_embeddings=True).tolist()
    top = index.query(vector=q_vec, top_k=1).matches[0]
    results.append((question, expected, top.id, top.score))

correct = 0
for question, expected, top_id, score in results:
    ok = grade(expected, top_id, score)
    print("✅" if ok else "❌", f"{score:.3f}", top_id, "|", question)
    correct += ok
print(f"\nScore: {correct}/{len(results)}")