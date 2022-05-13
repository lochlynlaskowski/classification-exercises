import pandas as pd
import numpy as np
import os
from env import get_db_url
    
    
def get_titanic_data():
    filename = 'titanic_data.csv'

    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
       sql_query = 'SELECT * FROM passengers'
       
    
    df = pd.read_sql(sql_query, get_db_url('titanic_db'))

    df.to_csv(filename)

    return df

############

def get_iris_data():
    filename = 'iris_data.csv'

    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
       sql_query = """
                SELECT 
                    species_id,
                    species_name,
                    sepal_length,
                    sepal_width,
                    petal_length,
                    petal_width
                FROM measurements
                JOIN species USING(species_id)
                """
    
    df = pd.read_sql(sql_query, get_db_url('iris_db'))

    df.to_csv(filename)

    return df


############



def get_telco_data():
    filename = 'telco_data.csv'

    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
       sql_query = '''SELECT * from customers
                JOIN contract_types using (contract_type_id)
                JOIN internet_service_types using (internet_service_type_id)
                JOIN payment_types using (payment_type_id)'''
       
    
    df = pd.read_sql(sql_query, get_db_url('telco_churn'))

    df.to_csv(filename)

    return df