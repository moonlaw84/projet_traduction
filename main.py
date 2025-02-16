from fastapi import FastAPI

# Création de l'application FastAPI
app = FastAPI()

# Définir une route principale
@app.get("/")
def home():
    return {"message": "Bienvenue sur l'API de traduction juridique FR-AR"}

# Route pour tester l'API
@app.get("/translate/")
def translate(text: str):
    return {"original_text": text, "translated_text": "Traduction non implémentée"}
from fastapi import FastAPI
from pydantic import BaseModel
from googletrans import Translator  # Assurez-vous d'avoir installé googletrans

app = FastAPI()

# Définition du modèle de requête
class TranslationRequest(BaseModel):
    text: str
    source_language: str
    target_language: str

# Endpoint POST pour la traduction
@app.post("/translate/")
async def translate(request: TranslationRequest):
    translator = Translator()
    translated = translator.translate(request.text, src=request.source_language, dest=request.target_language)
    return {"translated_text": translated.text}

# Endpoint GET de test
@app.get("/")
async def home():
    return {"message": "Bienvenue sur l'API de traduction juridique"}
