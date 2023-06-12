# Project Plan

## Summary

<!-- Describe your data science project in max. 5 sentences. -->
In our data science project, we are analyzing the number of bike riders in Cologne, Germany, and correlating it with air quality data from the Umweltbundesamt. Specifically, we are investigating the potential impact of increased bike ridership on reducing nitrogen dioxide (NO2) levels in Cologne. By examining the relationship between bike ridership and NO2 concentrations over a period of time, we aim to identify any patterns or trends that suggest a possible reduction in NO2 levels due to increased bike usage. This analysis can provide valuable insights for policymakers and urban planners seeking to improve air quality in the city.

## Rationale

<!-- Outline the impact of the analysis, e.g. which pains it solves. -->
Our project is relevant because it addresses the critical public health issue of reducing NO2 levels in cities like Cologne by examining the potential impact of increased bike ridership on air quality. This analysis can provide valuable insights for policymakers and urban planners seeking to promote sustainable transportation options and improve air quality in the city.

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->


### Datasource1: Air data from Umweltbundesamt
* Metadata URL: https://www.umweltbundesamt.de/en/data/air/air-data/annual-tabulation/eJxrWpScv9B0UWXqEiMDI0MAMNIFtg==
* Data URL: https://www.umweltbundesamt.de/api/air_data/v2/annualbalances/csv?component=5&year=2021&lang=en (This is year 2021, we can modify the variable "year" in the link to get the other years)
* Data Type: CSV

The air quality index is based on the measured concentrations of three pollutants (nitrogen dioxide, particulate matter (PM₁₀) and ozone). 


### Datasource2: Fahrrad Verkehrsdaten Koeln
* Metadata URL: https://mobilithek.info/offers/-5190830568637332944
* Data URL: https://offenedaten-koeln.de/dataset/fahrrad-verkehrsdaten-koeln-0
* Data Type: CSV

This dataset contains the recordings of automatic counting stations for bicycle traffic in Cologne from 2015 onwards.

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Automated data pipeline [#1][i1]
2. Automated tests [#2][i2]
3. CI [#3][i3]
4. Deploy project using GitHub pages [#4][i4]
5. Complete exploratory data analysis
6. Writing final report

[i1]: https://github.com/leoreinmann/2023-amse-template/issues/1
[i2]: https://github.com/leoreinmann/2023-amse-template/issues/2
[i3]: https://github.com/leoreinmann/2023-amse-template/issues/3
[i4]: https://github.com/leoreinmann/2023-amse-template/issues/4
[i5]: https://github.com/leoreinmann/2023-amse-template/issues/5
[i6]: https://github.com/leoreinmann/2023-amse-template/issues/6