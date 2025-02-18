# Utiliser des types de données efficaces

Les types de données par défaut de pandas ne sont pas les plus économes en mémoire. Cette étape montre comment utiliser des types de données plus efficaces pour stocker des ensembles de données plus volumineux en mémoire.

```python
ts = make_timeseries(freq="30S", seed=0)
ts.to_parquet("timeseries.parquet")
ts = pd.read_parquet("timeseries.parquet")

# Convertir la colonne 'name' en type 'category' pour plus d'efficacité
ts2 = ts.copy()
ts2["name"] = ts2["name"].astype("category")

# Réduire les colonnes numériques aux types les plus petits possibles
ts2["id"] = pd.to_numeric(ts2["id"], downcast="unsigned")
ts2[["x", "y"]] = ts2[["x", "y"]].apply(pd.to_numeric, downcast="float")
```
