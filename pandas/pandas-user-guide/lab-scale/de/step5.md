# Andere Bibliotheken verwenden

Andere Bibliotheken wie Dask können Datensätze verarbeiten, die größer sind als der verfügbare Speicher. Dask bietet eine pandas-ähnliche API und kann Daten parallel verarbeiten.

```python
import dask.dataframe as dd

ddf = dd.read_parquet("data/timeseries/ts*.parquet", engine="pyarrow")

# Häufigkeiten berechnen mit Dask
ddf["name"].value_counts().compute()
```
