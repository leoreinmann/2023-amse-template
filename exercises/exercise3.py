import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.types import BIGINT, TEXT, FLOAT

# List of column indices to keep
indices_to_keep = [0, 1, 2, 12, 22, 32, 42, 52, 62, 72]


df = pd.read_csv('https://www-genesis.destatis.de/genesis/downloads/00/tables/46251-0021_00.csv',
                  encoding="iso-8859-1",  delimiter=';',
                  skiprows=6, usecols=indices_to_keep, dtype=str)


# Remove the last 4 rows
df = df.iloc[:-4]

# rename
column_name_mapping = {df.columns[0]: 'date',
           df.columns[1]: 'CIN', 
           df.columns[2]: 'name', 
           df.columns[3]: 'petrol', 
           df.columns[4]: 'diesel', 
           df.columns[5]: 'gas', 
           df.columns[6]: 'electro', 
           df.columns[7]: 'hybrid', 
           df.columns[8]: 'plugInHybrid', 
           df.columns[9]: 'others'}

df = df.rename(columns=column_name_mapping)


# Drop all invalid rows
df = df.drop(df[df.eq('-').any(axis=1)].index)


# Typecast the numbers from str to int
column_pandas_dtype_mapping = {
    'date':str,
    'CIN':str,
    'name':str,
    'petrol':int,
    'diesel':int,
    'gas':int,
    'electro':int,
    'hybrid':int,
    'plugInHybrid':int,
    'others':int
}

df = df.astype(column_pandas_dtype_mapping)

# Filter and keep rows with CIN having exactly 5 letters
df = df[df['CIN'].str.len() == 5]

# Delete every row where a negative integer is
integer_columns = df.select_dtypes(include='int64').columns

df = df[(df[integer_columns] > 0).all(axis=1)]


column_sql_dtype_mapping = {
    'date':TEXT,
    'CIN':TEXT,
    'name':TEXT,
    'petrol':BIGINT,
    'diesel':BIGINT,
    'gas':BIGINT,
    'electro':BIGINT,
    'hybrid':BIGINT,
    'plugInHybrid':BIGINT,
    'others':BIGINT
}


engine = create_engine('sqlite:///cars.sqlite')

df.to_sql('cars', con=engine, if_exists='replace', dtype=column_sql_dtype_mapping)