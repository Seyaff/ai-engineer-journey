import httpx

with httpx.stream(
    "POST",
    "http://127.0.0.1:8000/chat/stream",
    json={"message": "Explain the internet in 150 words", "session_id": "s1"},
    timeout=60,
) as response:
    for text in response.iter_text():
        print(text, end="", flush=True)
print()