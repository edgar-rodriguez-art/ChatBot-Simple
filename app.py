# Author: Edgar Rodriguez
# Simple ChatBot Example Without Training

# The author generated this text in part using GPT-3, OpenAI's large-scale language generation model.
# After generating the draft of the text, the author reviewed, edited, revised and test it.
# This project is licensed under the terms of the MIT License

from flask import Flask, render_template, request

app = Flask(__name__)

# Predefined questions and answers in Spanish
preguntas_respuestas = {
    "Hola": "¡Hola! ¿En qué puedo ayudarte?",
    "¿Cómo estás?": "Estoy bien, gracias por preguntar.",
    "Adiós": "¡Hasta luego!",
    "Default": "Lo siento, no entiendo tu pregunta."
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    respuesta = preguntas_respuestas.get(user_input, preguntas_respuestas["Default"])
    return respuesta

if __name__ == '__main__':
    app.run(debug=True)
