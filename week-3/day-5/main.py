from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
from pydantic import BaseModel
from groq import Groq
import groq


load_dotenv()

app = FastAPI()
client = Groq()

sessions = {}

class ChatRequest(BaseModel):
    message : str
    session_id:str





@app.post("/chat")
def chat(req: ChatRequest):
    if req.session_id not in sessions:
        sessions[req.session_id] = []
    history = sessions[req.session_id]

    user_msg = {"role": "user", "content": req.message}
    convo = [{"role": "system", "content": "You are a helpful assistant. Keep answers short."}] + history[-6:] + [user_msg]

    try:
        response = client.chat.completions.create(model="openai/gpt-oss-120b", messages=convo)
    except groq.RateLimitError:
        # TODO 1: raise HTTPException with status_code=429 and a friendly detail message
        raise HTTPException(status_code=429 , detail="Too many requests. Please wait a moment and try again")
    except groq.APIConnectionError:
        # TODO 2: raise HTTPException with status_code=503
        raise HTTPException(status_code=503 , detail="AI service is unreachable. Please try again shortly")
    except groq.APIStatusError:
        # TODO 3: raise HTTPException with status_code=502
        raise HTTPException(status_code=502 , detail="AI service returned an error. Please try again")
    

    reply = response.choices[0].message.content

    # TODO 4: NOW save both messages to history (user_msg, then the assistant reply)
    history.append(user_msg)
    history.append({"role": "assistant", "content": reply})

    return {"reply": reply, "turns": len(history) // 2}