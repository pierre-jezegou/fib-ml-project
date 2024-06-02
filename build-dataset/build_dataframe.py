'''Build dataset'''
import pandas as pd

RAW_DATA_FOLDER = '../data/'

def transform_uid(uic: int | float | str) -> str:
    '''Format UIC'''
    return str(uic).split(".", maxsplit=1)[0].zfill(10)

### TRANSFORMATIONS - PREPARE INDIVIDUAL DATASETS ###
# Transform frequentation in train stations
frequentation = pd.read_csv(RAW_DATA_FOLDER + 'frequentation-gares-raw.csv', delimiter=";", header=0)
frequentation["UIC"] = frequentation["UIC"].astype(str).str.zfill(10)
frequentation = frequentation.rename(columns={'Nom de la gare': 'Gare'})

frequentation.to_csv(RAW_DATA_FOLDER + 'generated/frequentation-gares.csv', index=False, sep=";")


# Transform wifi presence in train stations
wifi = pd.read_csv(RAW_DATA_FOLDER + 'gares-equipees-du-wifi-raw.csv', delimiter=";", header=0)
wifi["UIC"] = wifi["UIC"].apply(lambda uid: ("87"+str(uid).split(".", maxsplit=1)[0]).zfill(10))
wifi.to_csv(RAW_DATA_FOLDER + 'generated/gares-equipees-du-wifi.csv', index=False, sep=";")


### TRANSFORMATIONS - MERGE DATASETS ###
FILENAMES = [RAW_DATA_FOLDER + "gares-de-voyageurs.csv",
             RAW_DATA_FOLDER + "generated/frequentation-gares.csv",
             RAW_DATA_FOLDER + "gares-pianos.csv",
             RAW_DATA_FOLDER + "generated/gares-equipees-du-wifi.csv",
             ]

def merge_data_train_stations(filenames: list[str]) -> pd.DataFrame:
    '''Merge datasets'''
    result = pd.DataFrame()
    for filename in filenames:
        if filename is not None:
            if result.empty:
                result = pd.read_csv(filename, header=0, delimiter=';')
            else:
                data_pd = pd.read_csv(filename, header=0, delimiter=';')
                data_pd = data_pd.drop(columns=['Gare'])
                data_pd["UIC"] = data_pd["UIC"].apply(transform_uid)
                result = pd.merge(result, data_pd, on="UIC", how="left")

    return result

# Final train station merge
train_stations = merge_data_train_stations(FILENAMES)

# Drop columns
train_stations = train_stations.drop(columns=['Segmentation DRG'])
for column in train_stations.columns[10:21]:
    train_stations = train_stations.drop(columns=[column])

# Convert column names in english
train_stations = train_stations.rename(columns={
    'Nom': 'city_name',
    'Trigramme': 'trigram',
    'UIC': 'uic',
    'Segment(s) DRG': 'drg_segment',
    'Position géographique': 'geographical_position',
    'Code postal': 'postal_code',
    'Total Voyageurs 2022': 'total_passengers_2022',
    'Total Voyageurs + Non voyageurs 2022': 'total_passengers_and_non_passengers_2022',
    'Total Voyageurs 2015': 'total_passengers_2015',
    'Total Voyageurs + Non voyageurs 2015': 'total_passengers_and_non_passengers_2015',
    'Piano': 'piano',
    'Power&Station': 'power_station',
    'Baby-Foot': 'baby_foot',
    'Distr Histoires Courtes': 'distr_histoires_courtes',
    'total': 'total',
    'Service Wifi': 'wifi_service'
})
train_stations.rename(columns={'Code commune': 'city_code'}, inplace=True)
# COnvert city_code to string
train_stations["city_code"] = train_stations["city_code"].astype(str)


### INTEGRATION - CONSOLIDATED CITIES ##
# Add consolidated cities information
consolidated_cities = pd.read_csv(RAW_DATA_FOLDER + 'generated/consolidated-cities.csv', delimiter=";", header=0)

# Merge with train stations
result = pd.merge(train_stations, consolidated_cities, on="city_code")

result.to_csv('dataset.csv', sep=';', encoding='utf-8', index=False)
