
from flask import Flask, request, jsonify
import openai
import os
import random

app = Flask(__name__)

# Configuración de OpenAI
openai.api_key = os.getenv('OPENAI_API_KEY')

# Lista de URLs de audios pregrabados con tu voz clonada (reemplázalos con los reales)
AUDIO_RESPUESTAS = [
    "https://example.com/audios/respuesta1.mp3",
    "https://example.com/audios/respuesta2.mp3",
    "https://example.com/audios/respuesta3.mp3"
]

@app.route('/responder', methods=['POST'])
def responder():
    data = request.json
    mensaje = data.get('mensaje', '')
    
    # Generar respuesta en estilo señor tierno
    prompt = (
        "Responde como un señor mayor tierno, afectuoso y amable. "
        "Sé dulce y tranquilo. Aquí va el mensaje recibido:
" + mensaje
    )
    
    respuesta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    
    texto_respuesta = respuesta['choices'][0]['message']['content']
    
    # Elegir audio al azar de los pregrabados
    audio_url = random.choice(AUDIO_RESPUESTAS)
    
    return jsonify({
        'respuesta': texto_respuesta,
        'audio_url': audio_url
    })

if __name__ == '__main__':
    app.run()
