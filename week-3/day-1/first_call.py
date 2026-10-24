from dotenv import load_dotenv
from groq import Groq


load_dotenv()
client = Groq()

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {"role": "system", "content": "Answer like a strict coach, in 1 line."},
        {"role" : "user" , "content" : "Can you tell me how llm works under the hood and do the heavy part in 100 words"}
    ]
)



print(response.choices[0].message.content)
print(response.usage)