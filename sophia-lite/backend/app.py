from fastapi import FastAPI
from pydantic import BaseModel
from llm_bridge import get_llm_response
from safety import filter_response, medica_guardrail
from medica import MedicaGeometrica

app = FastAPI()
medica = MedicaGeometrica()

class Message(BaseModel):
    text: str

@app.get("/")
def root():
    return {"message": "Sophia Lite Public Safe Edition ONLINE"}

@app.post("/chat")
def chat(msg: Message):
    raw = get_llm_response(msg.text)
    safe = filter_response(raw)

    if "health" in msg.text.lower():
        insights = medica.analyze()
        return {"response": str(insights)}

    return {"response": safe}

@app.post("/medica/log")
def log_health(data: dict):
    return medica.log_entry(
        data["mood"],
        data["energy"],
        data["sleep"],
        data["stress"],
        data.get("notes", "")
    )

@app.get("/medica/analyze")
def analyze_health():
    return medica.analyze()