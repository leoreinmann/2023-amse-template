import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.types import BIGINT, TEXT, FLOAT


column_mapping = {
    0: TEXT,
    1: TEXT,
    2: TEXT,
    3: BIGINT,
    4: BIGINT,
    5: BIGINT,
    6: BIGINT,
    7: BIGINT,
    8: BIGINT,
    9: BIGINT
}

# List of column indices to keep
indices_to_keep = [0, 1, 2, 12, 22, 32, 42, 52, 62, 72]


df = pd.read_csv('https://www-genesis.destatis.de/genesis/downloads/00/tables/46251-0021_00.csv',
                  encoding="iso-8859-1",  delimiter=';',
                  skiprows=6, usecols=indices_to_keep, dtype=str)


# Remove the last 4 rows
df = df.iloc[:-4]

# rename
mapping = {df.columns[0]: 'date',
           df.columns[1]: 'CIN', 
           df.columns[2]: 'name', 
           df.columns[3]: 'petrol', 
           df.columns[4]: 'diesel', 
           df.columns[5]: 'gas', 
           df.columns[6]: 'electro', 
           df.columns[7]: 'hybrid', 
           df.columns[8]: 'plugInHybrid', 
           df.columns[9]: 'others'}

df = df.rename(columns=mapping)







column_mapping = {
    0: 'date',
    1: 'CIN',
    2: 'name',
    12: 'petrol',
    22: 'diesel',
    32: 'gas',
    42: 'electro',
    52: 'hybrid',
    62: 'plugInHybrid',
    72: 'others'
}


engine = create_engine('sqlite:///cars.sqlite')

df.to_sql('cars', con=engine, if_exists='replace')