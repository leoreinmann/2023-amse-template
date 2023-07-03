import shutil
import pandas as pd
import urllib.request as ur
import ssl
import zipfile
from pathlib import Path
from sqlalchemy import create_engine


Path("./exercises/tmp/").mkdir(parents=True, exist_ok=True)

url = "https://gtfs.rhoenenergie-bus.de/GTFS.zip"
filepath = "./exercises/tmp/exercise5.zip"

# SSL encryption error handling
ssl._create_default_https_context = ssl._create_unverified_context

ur.urlretrieve(url, "./exercises/tmp/exercise5.zip")

zip = zipfile.ZipFile("./exercises/tmp/exercise5.zip")
zip.extractall("./exercises/tmp/")


indices_to_keep = [0, 2, 4, 5, 6]


type_mapping = {
    "stop_id": int, 
    "stop_name": str, 
    "stop_lat": float, 
    "stop_lon": float, 
    "zone_id": int
}

df = pd.read_csv("./exercises/tmp/stops.txt", sep=",", encoding='utf-8', usecols=indices_to_keep, dtype=type_mapping)

df = df[df["zone_id"] == 2001]

df = df[(df["stop_lat"] >= -90) & (df["stop_lat"] <= 90)]
df = df[(df["stop_lon"] >= -90) & (df["stop_lon"] <= 90)]

df.dropna(subset=["stop_name", "stop_lat", "stop_lon"], inplace=True)

engine = create_engine('sqlite:///gtfs.sqlite')

df.to_sql('stops', con=engine, if_exists='replace', index=False)

shutil.rmtree("./exercises/tmp/") 