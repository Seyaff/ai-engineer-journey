from dotenv import load_dotenv
from groq import Groq
from pinecone import Pinecone
from sentence_transformers import SentenceTransformer

load_dotenv()
index = Pinecone().Index("faq")
model = SentenceTransformer("all-MiniLM-L6-v2")
llm = Groq()

REWRITE = False   # run once with False, once with True, and compare

# (question, expected chunk id). None = NOT in the FAQ, so it should be refused
tests = [
    ("How much is Botox?", "chunk-2"),
    ("whats the price of botox", "chunk-2"),
    ("Can I pay in installments?", "chunk-11"),
    ("can i pay in installementss", "chunk-11"),
    ("Is there parking?", "chunk-9"),
    ("When are you open on Saturday?", "chunk-8"),
    ("Is the first consultation free?", "chunk-4"),
    ("How long does lip filler last?", "chunk-3"),
    ("What happens if I miss my appointment?", "chunk-10"),
    ("Is Botox dangerous?", "chunk-12"),
    ("Do you do tattoo removal?", None),
    ("Who won the World Cup?", None),
    ("Can I bring my dog?", None),
    ("hi", None),
    ("Who is the ceo at anthropic", None),
    ("do you have taattooo removal service", None),   # fixed label: not offered, so it should be refused
]


def rewrite(q):
    r = llm.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {"role": "system", "content": "Fix spelling and rewrite the user's question as a clear, "
                                          "short question for searching a med spa FAQ. "
                                          "Return ONLY the rewritten question."},
            {"role": "user", "content": q},
        ],
    )
    return r.choices[0].message.content.strip()


# 1. Search once per question, and keep only the top match
results = []
for q, expected in tests:
    search_q = rewrite(q) if REWRITE else q
    q_vec = model.encode(search_q, normalize_embeddings=True).tolist()
    top = index.query(vector=q_vec, top_k=1).matches[0]
    results.append((q, expected, top.id, top.score))
    print(f"{top.score:.3f}  {top.id:9} expected={str(expected):9} {q}")
    if REWRITE:
        print(f"{'':27}↳ searched as: {search_q}")

# 2. Score every threshold using the SAME results
print(f"\nREWRITE = {REWRITE}")
for t in [0.25, 0.30, 0.35, 0.40, 0.45]:
    correct = 0
    for q, expected, top_id, score in results:
        if expected is None:
            ok = score < t
        else:
            ok = score >= t and top_id == expected
        correct += ok
    print(f"threshold {t:.2f}: {correct}/{len(results)} correct")