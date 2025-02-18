# 効率的なデータ型を使用する

Pandas のデフォルトのデータ型は、メモリ使用効率が最適ではありません。このステップでは、より大きなデータセットをメモリに格納するために、より効率的なデータ型を使用する方法を示します。

```python
ts = make_timeseries(freq="30S", seed=0)
ts.to_parquet("timeseries.parquet")
ts = pd.read_parquet("timeseries.parquet")

# Convert 'name' column to 'category' type for efficiency
ts2 = ts.copy()
ts2["name"] = ts2["name"].astype("category")

# Downcast numeric columns to their smallest types
ts2["id"] = pd.to_numeric(ts2["id"], downcast="unsigned")
ts2[["x", "y"]] = ts2[["x", "y"]].apply(pd.to_numeric, downcast="float")
```
