# Usar Outras Bibliotecas

Outras bibliotecas como Dask podem lidar com conjuntos de dados maiores do que a memória. Dask fornece uma API semelhante ao pandas e pode processar dados em paralelo.

```python
import dask.dataframe as dd

ddf = dd.read_parquet("data/timeseries/ts*.parquet", engine="pyarrow")

# Compute value counts using Dask
ddf["name"].value_counts().compute()
```
