# 将长表格格式转换为宽表格格式

现在我们将使用 `pivot` 函数把空气质量的长格式数据转换为宽格式。

```python
# 仅筛选二氧化氮（no2）数据
no2 = air_quality[air_quality["parameter"] == "no2"]

# 对每个地点（按地点分组）使用2个测量值（取前两行）
no2_subset = no2.sort_index().groupby(["location"]).head(2)

# 透视数据
no2_subset.pivot(columns="location", values="value")
```
