import csv
import pandas as pd
from sqlalchemy import create_engine

from models import Service

engine = create_engine('sqlite://', echo=False)

def write_csv_to_sql():
    organisation = pd.read_csv('../service.csv').dropna()
    print(organisation.shape)
    organisation.to_sql("organisation", con=engine, if_exists='replace', index_label='id')

def db_get_row(organisation_name):
    search_string = "SELECT * FROM organisation WHERE organisation = \'{}\'".format(organisation_name)
    sql_result = engine.execute(search_string).fetchone()
    if sql_result is None:
        print("Error query did not return a result ({} not found)".format(organisation_name))
        return None
    else:
        service = Service(sql_result)
        return service.query_as_json()

def init_inmem_db():
    write_csv_to_sql()

if __name__ == "__main__":
    db_get_row('The Julian Trust')