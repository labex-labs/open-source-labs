# Fusionner des tables en utilisant un identifiant commun

Nous allons ensuite ajouter les coordonnées des stations au tableau de mesures à l'aide de la fonction `merge`. Nous effectuerons un jointure gauche sur la colonne `location`.

```python
# Load the stations coordinates data
stations_coord = pd.read_csv("data/air_quality_stations.csv")

# Merge the air_quality and stations_coord dataframes
air_quality = pd.merge(air_quality, stations_coord, how="left", on="location")
```
