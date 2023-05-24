import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.types import BIGINT, TEXT, FLOAT


df = pd.read_csv('https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/rhein-kreis-neuss-flughafen-weltweit/exports/csv', on_bad_lines='warn',  delimiter=';')

engine = create_engine('sqlite:///airports.sqlite')





df.to_sql('airports', con=engine, if_exists='replace', index=False, 
          dtype={
            'column_1': BIGINT,
            'column_2': TEXT,
            'column_3': TEXT,
            'column_4': TEXT,
            'column_5': TEXT,
            'column_6': TEXT,
            'column_7': FLOAT,
            'column_8': FLOAT,
            'column_9': BIGINT,
            'column_10': FLOAT,
            'column_11': TEXT,
            'column_12': TEXT,
            'geo_punkt': TEXT})