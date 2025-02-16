from flask import Flask, request, jsonify
from transformers import MarianMTModel, MarianTokenizer

# Initialisation de l'application Flask
app = Flask(__name__)

# Charger le modèle et le tokenizer
model = MarianMTModel.from_pretrained('modele_traduction')
tokenizer = MarianTokenizer.from_pretrained('modele_traduction')

@app.route('/')
def home():
    return 'Bienvenue sur la plateforme de traduction juridique IA !'

@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    text = data.get('text', '')

    if not text:
        return jsonify({'error': 'Aucun texte fourni.'}), 400

    # Traduire le texte
    inputs = tokenizer(text, return_tensors="pt")
    translated = model.generate(**inputs)
    translation = tokenizer.decode(translated[0], skip_special_tokens=True)

    return jsonify({'translation': translation})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
