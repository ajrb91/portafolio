from pathlib import Path
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from openai import OpenAI

# Cargar variables del archivo
load_dotenv()

# Crear cliente Open AI
client = OpenAI()

# Cargar documentación simulada
DOC_PATH = Path("data/docs.txt")
DOCUMENT_TEXT = DOC_PATH.read_text(encoding="utf-8")

app = FastAPI(title="Movizzon POC - Document Questions and Answers")

from pathlib import Path
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from openai import OpenAI

# 1️⃣ Cargar variables del archivo .env
load_dotenv()

# 2️⃣ Crear cliente OpenAI
client = OpenAI()

# 3️⃣ Cargar documentación simulada
DOC_PATH = Path("data/docs.txt")
DOCUMENT_TEXT = DOC_PATH.read_text(encoding="utf-8")

app = FastAPI(title="Movizzon PoC - Document QA")

# Modelo de datos que recibirá el endpoint
class AskRequest(BaseModel):
    question: str

# Endpoint de prueba
@app.get("/health")
def health():
    return {"status": "ok"}

# Endpoint principal
@app.post("/ask")
def ask(req: AskRequest):

    prompt = f"""
Eres un asistente que responde SOLO usando la documentación entregada como base, usa palabras claves para determinar la respuesta en base al catalogo.
Si la respuesta no está en la documentación, responde:
"No encontré esa información en la documentación."

DOCUMENTACIÓN:
{DOCUMENT_TEXT}

PREGUNTA:
{req.question}
""".strip()

    response = client.responses.create(
        model="gpt-4o-mini",
        input=prompt
    )

    return {
        "question": req.question,
        "answer": response.output_text
    }
