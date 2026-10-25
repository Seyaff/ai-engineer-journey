from fastapi import FastAPI
from dotenv import load_dotenv
from pydantic import BaseModel
from groq import Groq
import json


load_dotenv()



app = FastAPI()
client = Groq()


sessions = {}


class ChatRequest(BaseModel):
    message : str
    session_id:str





@app.post("/chat")
def chat(req: ChatRequest):
    # TODO 1: if req.session_id is not in sessions, create an empty list for it
    if req.session_id not in sessions:
        sessions[req.session_id] = []
        

    history = sessions[req.session_id]

    # TODO 2: append the user's message to history
    sessions[req.session_id].append({"role" : "user" , "content" : req.message})

    convo = [{"role": "system", "content": "You are a helpful assistant. Keep answers short."}] + history[-6:]

    response = client.chat.completions.create(model="openai/gpt-oss-120b", messages=convo)
    reply = response.choices[0].message.content

    # TODO 3: append the AI's reply to history
    sessions[req.session_id].append({"role" : "assistant" , "content" : reply})

    return {"reply": reply, "turns": len(history) // 2}