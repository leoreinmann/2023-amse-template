import pandas as pd

# Data Extraction

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

# ['State / Measuring network', 'Station code', 'Station name',
# 'Station setting', 'Station type', 'Annual mean value in µg/m³',
# 'Number of hourly mean values above 200 µg/m³*']



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


print(df_bike_2022.columns)