# 加载更少的数据

我们可以只加载所需的列，而不是加载所有数据。在这里，我们展示两种从 Parquet 文件中加载更少数据的方法。

```python
# 选项 1：加载所有数据然后过滤
columns = ["id_0", "name_0", "x_0", "y_0"]
pd.read_parquet("timeseries_wide.parquet")[columns]

# 选项 2：仅加载请求的列
pd.read_parquet("timeseries_wide.parquet", columns=columns)
```
