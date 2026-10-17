from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime, timezone

app = FastAPI(title="AIO AI Backend", version="0.1.0")

app.add_middleware(
CORSMiddleware,
allow_origins=[""],
allow_methods=["GET", "POST", "DELETE", "OPTIONS"],
allow_headers=[""],
)

class ChatRequest(BaseModel):
message: str
session_id: str = "default"

@app.get("/")
def root():
return {"name": "AIO AI Backend", "status": "running"}

@app.get("/health")
def health():
return {"status": "ok", "service": "aio-ai-backend"}

@app.post("/chat")
def chat(request: ChatRequest):
return {
"reply": (
"AIO AI Backend ချိတ်ဆက်မှု အောင်မြင်ပါပြီ။ "
"AI Model မချိတ်ဆက်ရသေးတဲ့အတွက် ယခုအချိန်မှာ "
"စမ်းသပ်အဖြေကိုသာ ပြန်ပေးနေပါတယ်။"
),
"session_id": request.session_id,
"timestamp": datetime.now(timezone.utc).isoformat(),
"model_connected": False
}

@app.get("/memory/{session_id}")
def get_memory(session_id: str):
return {"session_id": session_id, "messages": []}

@app.delete("/memory/{session_id}")
def clear_memory(session_id: str):
return {"session_id": session_id, "cleared": True}
