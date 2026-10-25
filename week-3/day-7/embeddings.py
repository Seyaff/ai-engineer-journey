from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

docs = [
    "Refunds are available within 30 days of purchase.",
    "Our store opens at 9 AM and closes at 6 PM.",
    "To reset your password, click 'Forgot password' on the login page.",
    "We ship to Pakistan, UAE and the UK.",
    "Pizza toppings include pepperoni, olives and mushrooms.",
]
doc_vecs = model.encode(docs, normalize_embeddings=True)
print("shape:", doc_vecs.shape)

for query in ["How do I get my money back?", "I forgot my login",
              "Do you deliver to Dubai?", "What time can I come in?"]:
    q_vec = model.encode(query, normalize_embeddings=True)
    scores = doc_vecs @ q_vec
    ranked = sorted(zip(scores, docs), reverse=True)
    print(f"\nQ: {query}")
    for score, doc in ranked[:2]:
        print(f"  {score:.3f}  {doc}")