import pandas as pd
import sqlite3


## Data Extraction

df_air_2013 = pd.read_csv("https://www.umweltbundesamt.de/api/air_data/v2/annualbalances/csv?component=5&year=2013&lang=en", on_bad_lines='warn',  delimiter=';')

df_air_2014 = pd.read_csv("https://www.umweltbundesamt.de/api/air_data/v2/annualbalances/csv?component=5&year=2014&lang=en", on_bad_lines='warn',  delimiter=';')

df_air_2015 = pd.read_csv("https://www.umweltbundesamt.de/api/air_data/v2/annualbalances/csv?component=5&year=2015&lang=en", on_bad_lines='warn',  delimiter=';')

df_air_2016 = pd.read_csv("https://www.umweltbundesamt.de/api/air_data/v2/annualbalances/csv?component=5&year=2016&lang=en", on_bad_lines='warn',  delimiter=';')

df_air_2017 = pd.read_csv("https://www.umweltbundesamt.de/api/air_data/v2/annualbalances/csv?component=5&year=2017&lang=en", on_bad_lines='warn',  delimiter=';')

df_air_2018 = pd.read_csv("https://www.umweltbundesamt.de/api/air_data/v2/annualbalances/csv?component=5&year=2018&lang=en", on_bad_lines='warn',  delimiter=';')

df_air_2019 = pd.read_csv("https://www.umweltbundesamt.de/api/air_data/v2/annualbalances/csv?component=5&year=2019&lang=en", on_bad_lines='warn',  delimiter=';')

df_air_2020 = pd.read_csv("https://www.umweltbundesamt.de/api/air_data/v2/annualbalances/csv?component=5&year=2020&lang=en", on_bad_lines='warn',  delimiter=';')

df_air_2021 = pd.read_csv("https://www.umweltbundesamt.de/api/air_data/v2/annualbalances/csv?component=5&year=2021&lang=en", on_bad_lines='warn',  delimiter=';')

df_air_2022 = pd.read_csv("https://www.umweltbundesamt.de/api/air_data/v2/annualbalances/csv?component=5&year=2022&lang=en", on_bad_lines='warn',  delimiter=';')

#   ['State / Measuring network', 'Station code', 'Station name',
#   'Station setting', 'Station type', 'Annual mean value in µg/m³',
#   'Number of hourly mean values above 200 µg/m³*']



df_bike_2013 = pd.read_csv("https://offenedaten-koeln.de/sites/default/files/Radverkehr%20f%C3%BCr%20Offene%20Daten%20K%C3%B6ln%202013.csv", encoding="iso-8859-1",  delimiter=';')

df_bike_2014 = pd.read_csv("https://offenedaten-koeln.de/sites/default/files/Radverkehr%20f%C3%BCr%20Offene%20Daten%20K%C3%B6ln%202014.csv", encoding="iso-8859-1",  delimiter=';')

df_bike_2015 = pd.read_csv("https://offenedaten-koeln.de/sites/default/files/Radverkehr%20f%C3%BCr%20Offene%20Daten%20K%C3%B6ln%202015.csv", encoding="iso-8859-1",  delimiter=';')

df_bike_2016 = pd.read_csv("https://offenedaten-koeln.de/sites/default/files/Fahrrad_Zaehlstellen_Koeln_2016.csv", encoding="iso-8859-1",  delimiter=';')

df_bike_2017 = pd.read_csv("https://offenedaten-koeln.de/sites/default/files/Fahrrad_Zaehlstellen_Koeln_2017.csv", encoding="iso-8859-1",  delimiter=';')

df_bike_2018 = pd.read_csv("https://offenedaten-koeln.de/sites/default/files/Fahrrad_Zaehlstellen_Koeln_2018.csv", encoding="iso-8859-1",  delimiter=';')

df_bike_2019 = pd.read_csv("https://offenedaten-koeln.de/sites/default/files/Fahrrad_Zaehlstellen_Koeln_2019.csv", encoding="iso-8859-1",  delimiter=';')

df_bike_2020 = pd.read_csv("https://offenedaten-koeln.de/sites/default/files/Fahrrad_Zaehlstellen_Koeln_2020.csv", encoding="iso-8859-1",  delimiter=';')

df_bike_2021 = pd.read_csv("https://offenedaten-koeln.de/sites/default/files/Radverkehr%20f%C3%BCr%20Offene%20Daten%20K%C3%B6ln%202021.csv", encoding="iso-8859-1",  delimiter=';')

df_bike_2022 = pd.read_csv("https://offenedaten-koeln.de/sites/default/files/Radverkehr%20f%C3%BCr%20Offene%20Daten%20K%C3%B6ln%202022.csv", encoding="iso-8859-1",  delimiter=';')



#   ['Unnamed: 0', 'Deutzer Brücke', 'Hohenzollernbrücke', 'Neumarkt',
#   'Zülpicher Straße', 'Bonner Straße', 'Venloer Straße', 'Vorgebirgswall',
#   'Universitäts-straße', 'A.-Schütte-Allee', 'Vorgebirgspark',
#   'A.-Silbermann-Weg', 'Stadtwald', 'Niederländer Ufer',
#   'Rodenkirchener Brücke', 'Severinsbrücke', 'Hohe Pforte',
#   'Neusser Straße']

## Data Transformation

df_air_2013['year'] = 2013
df_air_2014['year'] = 2014
df_air_2015['year'] = 2015
df_air_2016['year'] = 2016
df_air_2017['year'] = 2017
df_air_2018['year'] = 2018
df_air_2019['year'] = 2019
df_air_2020['year'] = 2020
df_air_2021['year'] = 2021
df_air_2022['year'] = 2022

# Combine all dataframes
df_air_merged = pd.concat([df_air_2013, df_air_2014, df_air_2015, df_air_2016, df_air_2017, df_air_2018, df_air_2019, df_air_2020, df_air_2021, df_air_2022], ignore_index=True, sort=False)


df_bike_2013['year'] = 2013
df_bike_2014['year'] = 2014
df_bike_2015['year'] = 2015
df_bike_2016['year'] = 2016
df_bike_2016.rename(columns={"Jahr 2016": "Unnamed: 0"}, inplace=True)
df_bike_2017['year'] = 2017
df_bike_2018['year'] = 2018
df_bike_2018.rename(columns={"Jahr 2018": "Unnamed: 0"}, inplace=True)
df_bike_2019['year'] = 2019
df_bike_2019.rename(columns={"Jahr 2019": "Unnamed: 0"}, inplace=True)
df_bike_2020['year'] = 2020
df_bike_2020.rename(columns={"Jahr 2020": "Unnamed: 0"}, inplace=True)
df_bike_2021['year'] = 2021
df_bike_2022['year'] = 2022


# Combine all dataframes
df_bike_merged = pd.concat([df_bike_2013, df_bike_2014, df_bike_2015, df_bike_2016, df_bike_2017, df_bike_2018, df_bike_2019, df_bike_2020, df_bike_2021, df_bike_2022], ignore_index=True, sort=False)

# Rename month column
df_bike_merged.rename(columns={"Unnamed: 0": "month"}, inplace=True)

# Add column sum for each month
df_bike_merged['sum'] = df_bike_merged.sum(axis=1)



# Drop rows in air if the data is not from not in Cologne
df_air_merged = df_air_merged.dropna(subset=['Station name'])
df_air_merged = df_air_merged[df_air_merged['Station name'].str.contains(r'\bKöln \b', regex=True)]

# Drop rows in air if data is not from traffic
df_air_merged = df_air_merged[df_air_merged['Station type'] == "traffic"]



## Data Loading
conn = sqlite3.connect('./data/data.db')
c = conn.cursor()

df_bike_merged.to_sql('bikes', conn, if_exists='replace', index=False)
df_air_merged.to_sql('air', conn, if_exists='replace', index=False)

conn.close()


