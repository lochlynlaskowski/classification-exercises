import pandas as pd
import os
from env import get_db_url

def get_titanic_data():
    filename = "titanic.csv"

    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        url = get_db_url("titanic")
        query = "select * from customers"

        df = pd.read_sql(query, url)

        df.to_csv(filename)

        return df