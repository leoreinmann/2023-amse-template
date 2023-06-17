import pandas as pd
from sqlalchemy import create_engine
import numpy as np


column_mapping = {
    0: str,
    1: str,
    2: str,
    12: np.int32,
    22: np.int32,
    32: np.int32,
    42: np.int32,
    52: np.int32,
    62: np.int32,
    72: np.int32
}

# List of column indices to keep
indices_to_keep = [0, 1, 2, 12, 22, 32, 42, 52, 62, 72]


df = pd.read_csv('https://www-genesis.destatis.de/genesis/downloads/00/tables/46251-0021_00.csv',
                  encoding="iso-8859-1",  delimiter=';',
                  skiprows=6, usecols=indices_to_keep, dtype=column_mapping)


# Remove the last 4 rows
df = df.iloc[:-4]


print(df.iloc[:, 4])



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

# List of column indices to keep
indices_to_keep = [0, 1, 2, 12, 22, 32, 42, 52, 62, 72]

# Drop columns not in the list
indices_to_drop = set(range(df.shape[1])) - set(indices_to_keep)

#df = df.drop(df.columns[list(indices_to_drop)], axis=1)



engine = create_engine('sqlite:///cars.sqlite')

df.to_sql('cars', con=engine, if_exists='replace')