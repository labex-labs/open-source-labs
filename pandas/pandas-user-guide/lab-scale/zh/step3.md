# 使用高效的数据类型

Pandas的默认数据类型并非最节省内存的。此步骤展示了如何使用更高效的数据类型在内存中存储更大的数据集。

```python
ts = make_timeseries(freq="30S", seed=0)
ts.to_parquet("timeseries.parquet")
ts = pd.read_parquet("timeseries.parquet")

# 为提高效率，将'name'列转换为'category'类型
ts2 = ts.copy()
ts2["name"] = ts2["name"].astype("category")

# 将数值列向下转换为最小的数据类型
ts2["id"] = pd.to_numeric(ts2["id"], downcast="unsigned")
ts2[["x", "y"]] = ts2[["x", "y"]].apply(pd.to_numeric, downcast="float")
```
