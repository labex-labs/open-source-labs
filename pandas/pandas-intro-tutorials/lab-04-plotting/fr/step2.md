# Charger les données

Nous utiliserons des données de qualité de l'air pour ce tutoriel. Les données seront chargées à partir d'un fichier CSV dans un DataFrame Pandas.

```python
# Loading the data
air_quality = pd.read_csv("data/air_quality_no2.csv", index_col=0, parse_dates=True)
air_quality.head()
```
