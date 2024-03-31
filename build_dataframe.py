'''Build dataset'''
import pandas as pd

FILENAMES = ["data/gares-de-voyageurs.csv",
             "data/frequentation-gares.csv",
            "data/gares-pianos.csv",
            "data/gares-equipees-du-wifi.csv",
            ]

def transform_uid(uic: int | float | str) -> str:
    '''Format UIC'''
    return str(uic).split(".")[0].zfill(10)

### TRANSFORMATIONS
# Transform frequentation in train stations
frequentation = pd.read_csv('data/frequentation-gares-raw.csv', delimiter=";", header=0)
frequentation["UIC"] = frequentation["UIC"].astype(str).str.zfill(10)
frequentation = frequentation.rename(columns={'Nom de la gare': 'Gare'})

frequentation.to_csv('data/frequentation-gares.csv', index=False, sep=";")


# Transform wifi presence in train stations
wifi = pd.read_csv('data/gares-equipees-du-wifi-raw.csv', delimiter=";", header=0)
wifi["UIC"] = wifi["UIC"].apply(lambda uid: ("87"+str(uid).split(".")[0]).zfill(10))
wifi.to_csv('data/gares-equipees-du-wifi.csv', index=False, sep=";")



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


# Final merge
train_stations = merge_data_train_stations(FILENAMES)
prices = pd.read_csv('data/tarifs-tgv-inoui-ouigo.csv', delimiter=";", header=0)

departure_stations = train_stations.add_prefix("departure_")
arrival_stations = train_stations.add_prefix("arrival_")


prices["Gare origine - code UIC"] = prices["Gare origine - code UIC"].apply(transform_uid)
prices["Gare destination - code UIC"] = prices["Gare destination - code UIC"].apply(transform_uid)

prices_consilidated = prices.merge(departure_stations, how="left", left_on="Gare origine - code UIC", right_on="departure_UIC").merge(arrival_stations, how="left", left_on="Gare destination - code UIC", right_on="arrival_UIC")

prices_consilidated.to_csv("sncf_dataset.csv", sep=";")
