from machinetranslation import translator
from flask import Flask, render_template, request
#
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    """
    translate English to French
    """
    return translator.englishToFrench(textToTranslate)

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    """
    translate French to English
    """
    return translator.frenchToEnglish(textToTranslate)

@app.route("/")
def renderIndexPage():
    """
    Return the main index.html
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
