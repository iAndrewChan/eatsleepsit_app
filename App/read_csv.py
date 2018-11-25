import csv
import pandas as pd
from sqlalchemy import create_engine

from models import Service

engine = create_engine('sqlite://', echo=False)

def write_csv_to_sql():
    organisation = pd.read_csv('../service.csv').dropna()
    print(organisation.shape)
    organisation.to_sql("organisation", con=engine, if_exists='replace', index_label='id')

def read_row(organisation_name):
    search_string = "SELECT * FROM organisation WHERE organisation = \'{}\'".format(organisation_name)
    sql_result = engine.execute(search_string).fetchone()
    service = Service(sql_result)
    print(service.query_as_json())

write_csv_to_sql()
read_row('The Julian Trust')