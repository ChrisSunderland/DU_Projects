# **Predicting Tennis Match Outcomes**

## **Description**

This repository contains a project I completed with two other classmates from my
program. As the three of us are all tennis fans, we decided to analyze data
from men's professional tennis matches that were played between 2015 and 2017. We sought to identify which factors played the biggest role in determining whether a player ultimately won or lost a match. To do this, we first had to apply significant
transformations to the original dataset. Extensive cleaning and feature engineering was
required. In the final phase of the project, we used Decision Tree and Random Forest Classifiers to try to accurately predict if a player won or lost a match.

3 separate CSV files were used as the input data for this analysis. Each record
in these files contains statistics and relevant information from every Association
of Tennis Professionals (ATP) match that was played during the 2015, 2016,
and 2017 seasons. The files originally came from the following repository:

https://github.com/JeffSackmann/tennis_atp

## **Data Dictionary**

Descriptions of some of the key fields used in our analysis can be found below:

| Attribute | Type | Description |
|----------|----------|----------|
| surface | string | match playing surface (hard court, clay, or grass) |
| tourney_date | integer | tournament start date |
| score | string | match result |
| minutes | float | match length |
| round | string | tournament round |
| best_of | integer | tournament format (best of 3 or best of 5 sets) |
| age | float | player age |
| rank | float | player ATP ranking |
| ace | float | total number of aces |
| df | float | total number of double faults |
| svpt | float | total number of service points |
| 1stIn | float | total number of first serves made |
| 1stWon | float | total number of first-serve points won |
| 2ndWon | float | total number of second-serve points won |
| SvGms | float | total number of service games |
| bpSaved | float | total number of break points saved  |
| bpFaced  | float | total number of break points faced |


## **Required Packages**

The notebook associated with this project uses Python 3.9.12 as well as the following packages:

* matplotlib 3.5.1
* numpy 1.24.3
* pandas 1.4.2
* re 2.2.1
* seaborn 0.11.2
* sklearn 1.1.2
