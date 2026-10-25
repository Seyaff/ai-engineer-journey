from groq import Groq
from dotenv import load_dotenv
import json


load_dotenv()
client = Groq()
MODEL = "openai/gpt-oss-120b"


SYSTEM = "You are a helpful assistant . Keep answers short"

FACT_PROMPT = (
    "You maintain a JSON object of key facts about the user "
    "(name, goals, order numbers, problems). Given the current facts and a new "
    "user message, return the UPDATED facts as JSON. Only include facts the user "
    "explicitly stated. Keep old facts unless the user changes them."
)



def update_facts(facts , user_msg):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role" : "system" ,"content" : FACT_PROMPT},
            {"role": "user", "content": f"Current facts: {json.dumps(facts)}\nNew message: {user_msg}"}
        ],
        response_format={"type" : "json_object"}
    )
    
    
    text = response.choices[0].message.content
    print(f"the text from the facts function is here : {text}")
    
    
    try :
        return json.loads(text)
    except json.JSONDecodeError:
        return facts
    
    
facts = {}
messages = []


while True:
    user_input = input("You: ")
    if user_input == "quit":
        break

    messages.append({"role": "user", "content": user_input})


    facts = update_facts(facts , user_input)
    facts = json.dumps(facts)
    # TODO 3: update facts using update_facts()


    system_msg = {"role": "system", "content": SYSTEM + "\nKnown facts: " + json.dumps(facts)}
    convo = [system_msg] + messages[-6:]
    # TODO 4: build `convo`: one system message whose content is
    #         SYSTEM + "\nKnown facts: " + json.dumps(facts)
    #         followed by the last 6 messages
   
    response = client.chat.completions.create(model=MODEL, messages=convo)
    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})

    print("AI:", reply)
    print("   [facts:", facts, "| prompt_tokens:", response.usage.prompt_tokens, "]")