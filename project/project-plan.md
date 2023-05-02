# Project Plan

## Summary

<!-- Describe your data science project in max. 5 sentences. -->
This project analyzes carbon monoxide emissions from vehicular traffic between 2014 and 2021, with a focus on the potential impact of the COVID-19 pandemic. 
We will differentiate between personal cars and trucks and consider the age of the vehicles. 
The project aims to generate insights that can inform policy decisions and mitigate the environmental impact of vehicular traffic.

## Rationale

<!-- Outline the impact of the analysis, e.g. which pains it solves. -->
By analyzing carbon monoxide emissions from vehicular traffic and generating insights that can inform policy decisions, this project may contribute to efforts to reduce air pollution, which can have negative impacts on human health and the environment.

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: Verkehr in Kilometern (VK), Zeitreihe 2014-2021
* Metadata URL: https://mobilithek.info/offers/573358679854608384
* Data URL: https://www.kba.de/SharedDocs/Downloads/DE/Statistik/Kraftverkehr/VK/vk_2021.xlsx
* Data Type: XLSX

The statistic "Verkehr in Kilometer (VK)" presents annual mileage figures based on the characteristics of vehicle type, vehicle age, and fuel type and energy source.
The data refers to motor vehicles registered with official license plates in Germany and has been published annually since 2013. 

### Datasource2: Annual AQ statistics (AirBase & e-Reporting merged)
* Metadata URL: https://www.eea.europa.eu/data-and-maps/data/aqereporting-9
* Data URL: https://discomap.eea.europa.eu/App/AirQualityStatistics/index.html?Country=Germany&AirPollutant=CO&AirQualityStationType=Traffic
* Data Type: CSV

European air quality information reported by EEA member countries, including all EU Member States, as well as EEA cooperating and other reporting countries. 
The EEA’s air quality database consists of a multi-annual time series of air quality measurement data and calculated statistics for a number of air pollutants. 
It also contains meta-information on the monitoring networks involved, their stations and measurements, air quality modelling techniques, as well as air quality zones, assessment regimes, compliance attainments and air quality plans and programmes reported by the EU Member States and European Economic Area countries.

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Automated data pipeline [#1][i1]
2. Automated tests [#2][i1]
3. CI [#3][i1]
4. Deploy project using GitHub pages [#4][i1]


[i1]: https://github.com/leoreinmann/2023-amse-template/issues/1
[i2]: https://github.com/leoreinmann/2023-amse-template/issues/2
[i3]: https://github.com/leoreinmann/2023-amse-template/issues/3
[i4]: https://github.com/leoreinmann/2023-amse-template/issues/4

