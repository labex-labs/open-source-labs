# 他のライブラリを使用する

Dask のような他のライブラリは、メモリよりも大きいデータセットを扱うことができます。Dask は pandas に似た API を提供し、データを並列処理することができます。

```python
import dask.dataframe as dd

ddf = dd.read_parquet("data/timeseries/ts*.parquet", engine="pyarrow")

# Compute value counts using Dask
ddf["name"].value_counts().compute()
```
