# Charger moins de données

Au lieu de charger toutes les données, nous pouvons charger seulement les colonnes dont nous avons besoin. Ici, nous démontrons deux méthodes pour charger moins de données à partir du fichier parquet.

```python
# Option 1: Charger toutes les données puis filtrer
columns = ["id_0", "name_0", "x_0", "y_0"]
pd.read_parquet("timeseries_wide.parquet")[columns]

# Option 2: Charger seulement les colonnes demandées
pd.read_parquet("timeseries_wide.parquet", columns=columns)
```
