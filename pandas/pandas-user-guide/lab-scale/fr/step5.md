# Utiliser d'autres bibliothèques

D'autres bibliothèques telles que Dask peuvent gérer des ensembles de données plus volumineux que la mémoire disponible. Dask propose une API similaire à celle de pandas et peut traiter les données en parallèle.

```python
import dask.dataframe as dd

ddf = dd.read_parquet("data/timeseries/ts*.parquet", engine="pyarrow")

# Calculer les décomptes de valeurs à l'aide de Dask
ddf["name"].value_counts().compute()
```
