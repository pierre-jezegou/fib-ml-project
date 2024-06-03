# Project - Machine Learning Analysis of Train stations
- Pierre Jézégou
- Julie Oppedal

## Project
Understanding how many passengers use train stations and what features they have is important for improving transportation services. We’re using machine learning to analyze train station data and predict passenger traffic.

To start, we’re gathering data from reliable sources like the SNCF and INSEE websites to create a detailed dataset with lots of information about cities and train stations.
Next, we’re cleaning up the data to fix errors and make sure it’s good for analysis. Then, we’ll use different machine learning models to try and figure out the best way to predict passenger traffic and understand what factors make some stations busier than others.

Overall, this project focuses on using advanced computer techniques to optimize transportation services by accurately predicting passenger traffic and understanding station dynamics.

## Documents
- `project_proposal`: first deliverable
- `main`: final report

## Project organization
```plain
.
├── README.md
├── requirements.txt
│
├── documentation
│   ├── BUILD_DATASET.md
│   ├── NOTICE.md
│   ├── TODO.md
│   └── project_proposal.tex
│
├── data
│   ├── attraction_area_per_city.csv
│   ├── cities_statistics.csv
│   ├── frequentation-gares-raw.csv
│   ├── gares-de-voyageurs.csv
│   ├── gares-equipees-du-wifi-raw.csv
│   └── gares-pianos.csv
├── build-dataset
│   ├── build_dataframe.py
│   └── consolidate_cities.py
│
├── Preprocessing.ipynb
├── distance_calculation.py
├── dataRead_processed.pkl.bz2
├── dataset_preprocessed.csv
│
└── models
   ├── helpers.py
   ├── knn.ipynb
   ├── linear-models.ipynb
   ├── metrics.csv
   ├── randomforest.ipynb
   ├── sampling.ipynb
   └── svm.ipynb 
```
- `documentation`: contains all the documentation files
    - `BUILD_DATASET.md`: explains how to build the dataset manually (without the CI)
    - `NOTICE.md`: contains the notice for the project, to reproduce the results
- Build dataset
    - `data`: contains all the data files
    - `build-dataset`: contains the scripts to build the dataset
- Preprocessing notebook and algorithms are located at the root of the project
- `models`: contains the notebooks for the models

## Usage
- Install working environment
    - Install virtual environment (`venv`): `python3 -m venv .venv && source .venv/bin/activate`
    - Install dependencies & libraries : `pip install -r requirements.txt`

- Train the model
- Use the model



## Features

| Feature                                      | Description                                           | Data Type | Number of Unique Values |
| -------------------------------------------- | ----------------------------------------------------- | --------- | ---------------------- |
| city_name                                    | Name of the city                                      | string    | String  |
| Trigramme                                    | Trigram of the city                                   | string    | String  |
| drg_segment                                  | DRG segment                                           | string    | Categorical |
| geographical_position                        | Geographical position                                | string    | String  |
| city_code                                    | City code                                             | string    | String  |
| uic                                          | UIC code                                              | string    | String  |
| postal_code                                  | Postal code                                           | string    | String  |
| total_passengers_2022                        | Total passengers in 2022                              | integer   | Integer |
| total_passengers_and_non_passengers_2022     | Total passengers and non-passengers in 2022           | integer   | Integer |
| Total Voyageurs 2021                         | Total passengers in 2021                              | integer   | Integer |
| total_passengers_2015                        | Total passengers in 2015                              | integer   | Integer |
| total_passengers_and_non_passengers_2015     | Total passengers and non-passengers in 2015           | integer   | Integer |
| piano                                        | Piano                                                 | string    | Categorical |
| power_station                                | Power station                                         | string    | Categorical |
| baby_foot                                    | Baby foot                                             | string    | Categorical |
| distr_histoires_courtes                      | Distribution of short stories                         | string    | Categorical |
| total                                        | Total                                                 | string    | Categorical |
| wifi_service                                 | WiFi service                                          | string    | Categorical |
| Unnamed: 0                                   | Unnamed column                                        | string    | Categorical |
| city_label                                   | City label                                            | string    | Categorical |
| city_attraction_area                         | City attraction area                                  | string    | Categorical |
| city_attraction_label                        | City attraction label                                 | string    | Categorical |
| department                                   | Department                                            | string    | Categorical |
| region                                       | Region                                                | string    | Categorical |
| sum_municipal_population_2021                | Sum of municipal population in 2021                   | integer   | Integer |
| non_scholarized_15_years_old_or_more_2020    | Number of non-scholarized individuals aged 15 or more in 2020 | integer | Integer |
| main_residences_2020                         | Number of main residences in 2020                     | integer   | Integer |
| housing_2020                                 | Housing in 2020                                      | integer   | Integer |
| jobs_at_workplace_2020                       | Number of jobs at workplace in 2020                   | integer   | Integer |
| active_employers_2021                        | Number of active employers in 2021                    | integer   | Integer |
| hotels_2024_sum                              | Sum of hotels in 2024                                | integer   | Integer |
| hotel_rooms_2024_sum                         | Sum of hotel rooms in 2024                           | integer   | Integer |
| camping_sites_2024_sum                       | Sum of camping sites in 2024                          | integer   | Integer |
| camping_sites_2024_sum.1                     | Sum of camping sites in 2024                          | integer   | Integer |
| other_tourist_accommodations_2024_sum         | Sum of other tourist accommodations in 2024           | integer   | Integer |
