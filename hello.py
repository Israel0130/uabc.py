from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Bienvenido a casa!</p>"

@app.route("/about")
def sobredemi():
    return "Hola soy isra"
