from dotenv import load_dotenv
from groq import Groq
from sentence_transformers import SentenceTransformer

load_dotenv()
client = Groq()
model = SentenceTransformer("all-MiniLM-L6-v2")

docs = [
    "Refunds are available within 30 days of purchase.",
    "Our store opens at 9 AM and closes at 6 PM.",
    "To reset your password, click 'Forgot password' on the login page.",
    "We ship to Pakistan, UAE and the UK.",
    "Pizza toppings include pepperoni, olives and mushrooms.",
]
doc_vecs = model.encode(docs, normalize_embeddings=True)
print(f"the docs vecs : {doc_vecs}")


def retrieve(query, k=2):
    q_vec = model.encode(query, normalize_embeddings=True)
    scores = doc_vecs @ q_vec
    ranked = sorted(zip(scores, docs), reverse=True)
    return ranked[:k]





def answer(query):
    
    top = retrieve(query)
    best_score = top[0][0]
    if best_score < 0.35:
        return top, "I don't know. (no relevant document found)"
    context = "\n".join(doc for score, doc in top)
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {"role": "system", "content":
                "Answer ONLY using the context below. If the answer is not in the "
                "context, say \"I don't know.\"\n\nContext:\n" + context},
            {"role": "user", "content": query},
        ],
    )
    return top, response.choices[0].message.content


for q in ["Can I return something I bought 2 weeks ago?",
          "Do you deliver to Dubai?",
          "Do you sell burgers?",
          "Who is the CEO?"]:
    top, reply = answer(q)
    print(f"\nQ: {q}")
    print(f"  retrieved: {[round(float(s), 3) for s, d in top]}")
    print(f"  AI: {reply}")
