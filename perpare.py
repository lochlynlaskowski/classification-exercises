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


########## TELCO DATA ###########
def prep_telco(df):
    df['total_charges'] = df['total_charges'].str.strip()
    df = df[df.total_charges != '']
    df['total_charges'] = df.total_charges.astype(float)
    columns_to_drop = ['Unnamed: 0','internet_service_type_id', 'payment_type_id', 'contract_type_id']
    df = df.drop(columns = columns_to_drop)
    df['is_female'] = df['gender'].map({'Female': 1, 'Male': 0})
    df['has_partner'] = df['partner'].map({'Yes': 1, 'No': 0})
    df['has_dependents'] = df['dependents'].map({'Yes': 1, 'No': 0})
    df['has_phone_service'] = df['phone_service'].map({'Yes': 1, 'No': 0})
    df['has_paperless_billing'] = df['paperless_billing'].map({'Yes': 1, 'No': 0})
    df['has_churned'] = df['churn'].map({'Yes': 1, 'No': 0})
    
    dummy_df = pd.get_dummies(df[['gender', 'partner', 'phone_service', \
                                  'multiple_lines', 'online_security', \
                                  'online_backup', 'tech_support', \
                                  'streaming_tv', 'streaming_movies', \
                                  'paperless_billing', 'churn', 'contract_type', \
                                  'internet_service_type', 'payment_type']], \
                              dummy_na=False, drop_first=False)
    df = pd.concat([df, dummy_df], axis=1)
    return df

    ############## TITANIC DATA ##############
    def clean_titanic_data(df):
    '''
    Takes in a titanic dataframe and returns a cleaned dataframe
    Arguments: df - a pandas dataframe with the expected feature names and columns
    Return: clean_df - a dataframe with the cleaning operations performed on it
    '''
    # Drop duplicates
    df.drop_duplicates(inplace=True)
    # Drop columns 
    columns_to_drop = ['embarked', 'class', 'passenger_id', 'deck', 'Unnamed: 0']
    df = df.drop(columns = columns_to_drop)
    # encoded categorical variables
    dummy_df = pd.get_dummies(df[['sex', 'embark_town']], dummy_na=False, drop_first=[True, True])
    df = pd.concat([df, dummy_df], axis=1)
    return df.drop(columns=['sex', 'embark_town'])  

    def impute_age(train, validate, test):
    '''
    Imputes the mean age of train to all three datasets
    '''
    imputer = SimpleImputer(strategy='mean', missing_values=np.nan)
    imputer = imputer.fit(train[['age']])
    train[['age']] = imputer.transform(train[['age']])
    validate[['age']] = imputer.transform(validate[['age']])
    test[['age']] = imputer.transform(test[['age']])
    return train, validate, test

    def prep_titanic_data(df): 
    df = clean_titanic_data(df)
    train, test = train_test_split(df,
                               train_size = 0.8,
                               stratify = df.survived,
                               random_state=1234)
    train, validate = train_test_split(train,
                                  train_size = 0.7,
                                  stratify = train.survived,
                                  random_state=1234)
    train, validate, test = impute_age(train, validate, test)
    return train, validate, test