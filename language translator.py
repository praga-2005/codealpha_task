from flask import Flask, render_template, request, jsonify
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/translate", methods=["POST"])
def translate():
    data = request.get_json()
    text = data.get("text", "")
    target_lang = data.get("target_lang", "es")  # Default to Spanish if none provided

    if text:
        translated = translator.translate(text, dest=target_lang)
        return jsonify({"translated_text": translated.text})
    
    return jsonify({"translated_text": "Error: No text provided"})

if __name__ == "__main__":
    app.run(debug=True)
