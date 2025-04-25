# 使用其他库

像 Dask 这样的其他库可以处理大于内存的数据集。Dask 提供了类似 pandas 的 API，并且可以并行处理数据。

```python
import dask.dataframe as dd

ddf = dd.read_parquet("data/timeseries/ts*.parquet", engine="pyarrow")

# 使用 Dask 计算值计数
ddf["name"].value_counts().compute()
```
