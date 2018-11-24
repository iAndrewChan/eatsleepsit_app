from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

@app.route("/eat")
def eat_page():
    return "eat World!"

@app.route("/help")
def help_page():
    return "help World!"

@app.route("/sleep")
def sleep_page():
    return "sleep World!"

@app.route("/contact")
def contact_page():
    return "contact page"