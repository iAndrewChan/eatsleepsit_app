from flask import Flask
from flask import g
import sqlite3
from database import db_session
from database import init_db
from models import Organisation
app = Flask(__name__)

@app.route("/")
def index():
    # db_session()
    # init_db()
    print(Organisation.query.all())
    print(Organisation.query.filter(Organisation.name == 'admin').first())
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

########
# Database

# @app.teardown_appcontext
# def close_connection(exception):
#     db = getattr(g, '_database', None)
#     if db is not None:
#         db.close()
########
