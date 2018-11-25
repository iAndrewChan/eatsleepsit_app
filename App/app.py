from flask import Flask
from flask import g
import sqlite3
# from database import db_session
# from database import init_db
# from models import Organisation

# from read_csv import init_inmem_db
# from read_csv import db_get_row

from flask import render_template

app = Flask(__name__)

@app.route("/")
@app.route("/<organisation_name>")
def index(organisation_name='The Salvation Army Logos House'):
    # db_session()
    # init_db()
    # print(Organisation.query.all())
    # print(Organisation.query.filter(Organisation.name == 'admin').first())

    # init_inmem_db()
    # table_row = db_get_row(organisation_name)
    # print(table_row)


    return render_template('Homepage.html')

@app.route("/contacts")
def contacts_page():
    return render_template('ContactPage.html')

@app.route("/help")
def help_page():
    return "help World!"

@app.route("/eat")
def eat_page():
    return render_template('EatPage.html') 

@app.route("/sleep")
def sleep_page():
    return render_template('SleepPage.html') 

@app.route("/sitting")
def sit_page():
    return render_template('SitPage.html') 



########
# Database

# @app.teardown_appcontext
# def close_connection(exception):
#     db = getattr(g, '_database', None)
#     if db is not None:
#         db.close()
########
