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
