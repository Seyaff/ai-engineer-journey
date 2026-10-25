from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
from fastapi.responses import StreamingResponse
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





@app.post("/chat/stream")
def chat_stream(req: ChatRequest):
    if req.session_id not in sessions:
        sessions[req.session_id] = []
    history = sessions[req.session_id]

    user_msg = {"role": "user", "content": req.message}
    convo = [{"role": "system", "content": "You are a helpful assistant."}] + history[-6:] + [user_msg]

    def generate():
        parts = []
        stream = client.chat.completions.create(
            model="openai/gpt-oss-120b", messages=convo, stream=True
        )
        for chunk in stream:
            piece = chunk.choices[0].delta.content
            if piece:
                parts.append(piece)
                print(piece)
                # TODO 1: send this piece to the client right now
                yield piece

        # TODO 2: the stream has finished, so save user_msg + the full reply to history
        #         (hint: join the parts into one string)
        whole_reply = "".join(parts)
        history.append(user_msg)
        history.append({"role": "assistant", "content": whole_reply})

    return StreamingResponse(generate(), media_type="text/plain")