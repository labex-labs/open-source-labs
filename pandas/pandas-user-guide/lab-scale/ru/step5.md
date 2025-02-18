# Использование других библиотек

Другие библиотеки, такие как Dask, могут обрабатывать наборы данных, размер которых превышает объем памяти. Dask предоставляет API, похожее на API pandas, и может обрабатывать данные параллельно.

```python
import dask.dataframe as dd

ddf = dd.read_parquet("data/timeseries/ts*.parquet", engine="pyarrow")

# Вычисление частот значений с использованием Dask
ddf["name"].value_counts().compute()
```
