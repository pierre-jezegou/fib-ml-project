"""
Consolidates city statistics and attraction area data into a single dataset.
    Reads two CSV files: 'cities_statistics.csv' and 'attraction_area_per_city.csv'.
    Performs data cleaning and merging operations on the datasets.
    Calculates the sum of numerical data per 'Aire d'attraction des villes 2020'.
    Translates column names to English.
    Saves the consolidated dataset as 'consolidated-cities.csv'.
"""
import pandas as pd

# Load the data
cities_statistics = pd.read_csv('data/cities_statistics.csv', delimiter=";", header=2)
cities_attraction = pd.read_csv('data/attraction_area_per_city.csv', delimiter=";", header=0)

# Change column types
cities_statistics = cities_statistics.convert_dtypes()
cities_attraction = cities_attraction.convert_dtypes()
for column in cities_statistics.columns[2:]:
    cities_statistics[column] = pd.to_numeric(cities_statistics[column], errors='coerce')

# Create common key
cities_statistics = cities_statistics.rename(columns={'Code': 'city_code'})
cities_attraction = cities_attraction.rename(columns={'Code géographique': 'city_code'})

# Merge datasets on `city_code`
result = pd.merge(cities_attraction, cities_statistics, on="city_code")


sum_per_attraction = result.groupby("Aire d'attraction des villes 2020").sum()

# Keep only numerical data and 'Aire d'attraction des villes 2020" column
sum_per_attraction = result.select_dtypes(include='number')
sum_per_attraction["Aire d'attraction des villes 2020"] = result["Aire d'attraction des villes 2020"]
sum_per_attraction = sum_per_attraction.drop(columns=["Région",
                                                      "Catégorie commune dans aire d'attraction des villes 2020"])

# Sum data per `Aire d'attraction des villes 2020`
sum_per_attraction = sum_per_attraction.groupby("Aire d'attraction des villes 2020").sum()

# Merge with the original dataset
merged_data = pd.merge(cities_attraction,
                       sum_per_attraction,
                       on="Aire d'attraction des villes 2020",
                       suffixes=('', '_sum'))

# Translate column names to english
merged_data = merged_data.rename(columns={
    'Code géographique': 'city_code',
    'Libellé géographique': 'city_label',
    'Libellé aire d\'attraction des villes 2020': 'city_attraction_label',
    'Aire d\'attraction des villes 2020': 'city_attraction_area',
    'Département': 'department',
    'Région': 'region',
    'Population municipale 2021': 'sum_municipal_population_2021',
    'Nb de pers. non scolarisées de 15 ans ou + 2020': 'non_scholarized_15_years_old_or_more_2020',
    'Résidences principales 2020': 'main_residences_2020',
    'Logements 2020': 'housing_2020',
    'Nb d\'emplois au lieu de travail (LT) 2020': 'jobs_at_workplace_2020',
    'Nb étab. actifs employeurs au 31/12 2021': 'active_employers_2021',
    'Nb d\'hotels 2024': 'hotels_2024',
    'Population municipale 2021_sum': 'municipal_population_2021_sum',
    'Nb etab. actifs employeurs au 31/12 2021_sum': 'active_employers_2021_sum',
    'Nb d\'hôtels 2024': 'hotels_2024_sum',
    'Nb de chambres dans les hôtels 2024': 'hotel_rooms_2024_sum',
    'Nb de terrains de camping 2024': 'camping_sites_2024_sum',
    'Nb d\'emplacements de camping 2024': 'camping_sites_2024_sum',
    'Nb d\'autres hébergements collectifs de tourisme 2024': 'other_tourist_accommodations_2024_sum',
    'Catégorie commune dans aire d\'attraction des villes 2020': 'city_category_in_attraction_area_2020'
})
print(merged_data.dtypes)
merged_data.to_csv('data/generated/consolidated-cities.csv', sep=';', encoding='utf-8', index=False)
