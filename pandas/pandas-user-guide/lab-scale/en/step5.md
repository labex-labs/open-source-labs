# Use Other Libraries

Other libraries like Dask can handle larger-than-memory datasets. Dask provides a pandas-like API and can process data in parallel.

```python
import dask.dataframe as dd

ddf = dd.read_parquet("data/timeseries/ts*.parquet", engine="pyarrow")

# Compute value counts using Dask
ddf["name"].value_counts().compute()
```
