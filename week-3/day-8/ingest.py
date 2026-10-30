import time
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec
from sentence_transformers import SentenceTransformer

load_dotenv()
pc = Pinecone()
model = SentenceTransformer("all-MiniLM-L6-v2")

INDEX = "faq"
if not pc.has_index(INDEX):
    pc.create_index(
        name=INDEX,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1"),
    )
index = pc.Index(INDEX)

# clear old chunks (learning only, never on a real client's index)
index.delete(delete_all=True)

with open("week-3/day-8/faq.txt", encoding="utf-8") as f:
    text = f.read()

# chunk by Q&A: split at blank lines
chunks = [c.strip() for c in text.split("\n\n") if c.strip()]
print(f"Yeh chunks hai bhaiya : {chunks}")
print("characters:", len(text), "| chunks:", len(chunks))

vecs = model.encode(chunks, normalize_embeddings=True)

index.upsert(vectors=[
    {"id": f"chunk-{i}", "values": vec.tolist(), "metadata": {"text": chunk}}
    for i, (chunk, vec) in enumerate(zip(chunks, vecs))
])
print("uploaded", len(chunks), "chunks")
time.sleep(10)

