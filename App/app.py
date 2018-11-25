from flask import Flask
from flask import g
import sqlite3
# from database import db_session
# from database import init_db
# from models import Organisation

from read_csv import init_inmem_db
from read_csv import db_get_row

from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    # db_session()
    # init_db()
    # print(Organisation.query.all())
    # print(Organisation.query.filter(Organisation.name == 'admin').first())

    return render_template('Homepage.html')

@app.route("/organisation")
@app.route("/organisation/<organisation_name>")
def organisation(organisation_name='The Julian Trust'):
    # db_session()
    # init_db()
    # print(Organisation.query.all())
    # print(Organisation.query.filter(Organisation.name == 'admin').first())

    init_inmem_db()
    table_row = db_get_row(organisation_name)

    if table_row is None:
        return render_template('Homepage.html')
    else:
        print(table_row)
        return render_template('OrganisationPage.html', organisation=table_row)



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
