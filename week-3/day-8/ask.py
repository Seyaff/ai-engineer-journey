from dotenv import load_dotenv
from groq import Groq
from pinecone import Pinecone
from sentence_transformers import SentenceTransformer

load_dotenv()
llm = Groq()
index = Pinecone().Index("faq")
model = SentenceTransformer("all-MiniLM-L6-v2")
THRESHOLD = 0.30


def retrieve(question, k=3):
    q_vec = model.encode(question, normalize_embeddings=True).tolist()
    res = index.query(vector=q_vec, top_k=k, include_metadata=True)
    
    return [m for m in res.matches if m.score >= THRESHOLD]


def retrieve(question, k=3):
    q_vec = model.encode(question, normalize_embeddings=True).tolist()
    res = index.query(vector=q_vec, top_k=k, include_metadata=True)
    return res.matches            # return ALL matches; filter in answer()


def answer(question):
    all_matches = retrieve(question)
    matches = [m for m in all_matches if m.score >= THRESHOLD]
    if not matches:
        best = all_matches[0].score if all_matches else 0
        return f"I don't know. Please contact the clinic directly. (best score {best:.3f}, below {THRESHOLD})", []

    context = "\n\n".join(f"[{m.id}] {m.metadata['text']}" for m in matches)
    response = llm.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {"role": "system", "content":
                "You are the front-desk assistant for Glow Haven Med Spa. "
                "Answer ONLY from the context. Cite the chunk id you used, like [chunk-2]. "
                "If the answer isn't in the context, say you don't know.\n\nContext:\n" + context},
            {"role": "user", "content": question},
        ],
    )
    return response.choices[0].message.content, [(m.id, round(m.score, 3)) for m in matches]


while True:
    q = input("\nYou: ")
    if q == "quit":
        break
    reply, sources = answer(q)
    print("AI:", reply)
    print("   sources:", sources)