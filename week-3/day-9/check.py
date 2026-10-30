from dotenv import load_dotenv
from pinecone import Pinecone
from sentence_transformers import SentenceTransformer

load_dotenv()
index = Pinecone().Index("faq")
model = SentenceTransformer("all-MiniLM-L6-v2")

tests = [
    # --- set 1 (from Day 9) ---
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
    ("do you have taattooo removal service", None),

    # --- set 2 (today) ---
    ("Is there a monthly subscription?", "chunk-13"),
    ("Will my face be red after microneedling?", "chunk-7"),
    ("where r u located", "chunk-9"),
    ("Can pregnant women get Botox?", "chunk-12"),
    ("How many laser sessions will I need?", "chunk-6"),
    ("Do you sell skincare products?", None),
    ("Can I come in on Sunday?", "chunk-8"),
    ("What's the weather in Santa Monica?", None),
    ("how much for a hydrafacial", "chunk-5"),
    ("Do you accept insurance?", None),
]


results = []

for question , expected in tests:
    q_vec = model.encode(question, normalize_embeddings=True).tolist()
    top = index.query(vector=q_vec, top_k=1).matches[0]
    results.append((question , expected , top.id , top.score))
    print(f"{top.score:.3f}  {top.id:9} expected={str(expected):9} {question}")
  
    
    
    
THRESHOLDS = [0.25, 0.30, 0.35, 0.40, 0.45]

for t in THRESHOLDS:
    correct = 0
    for q, expected, top_id, score in results:
        if expected is None:
            ok = score < t                           # should be refused
        else:
            ok = score >= t and top_id == expected   # should pass + right chunk
        correct += ok
    print(f"threshold {t:.2f}: {correct}/{len(results)} correct")