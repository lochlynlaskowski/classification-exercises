import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer



def prep_iris(df):
    columns_to_drop = ['species_id', 'Unnamed: 0', 'measurement_id']
    df = df.drop(columns = columns_to_drop)
    df = df.rename(columns = {'species_name':'species'}, inplace = True)
    dummy_df = pd.get_dummies(df_iris[['species']], dummy_na=False, drop_first=[True])
    df = pd.concat([df, dummy_df], axis=1)
    return df



