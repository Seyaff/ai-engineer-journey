from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq()

messages = [
    {"role": "system", "content": "You are a helpful assistant. Keep answers short."}
]

while True:
    user_input = input("You: ")
    if user_input == "quit":
        break

    messages.append({"role": "user", "content": user_input})

    recent = [messages[0]] + messages[-6:]     # rebuilt every turn

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=recent,
    )
    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})   # uncomment this

    print("AI:", reply)
    print("   [prompt_tokens:", response.usage.prompt_tokens, "]")
    
    
print(messages)