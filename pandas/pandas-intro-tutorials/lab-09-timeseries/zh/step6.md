# 重采样时间序列数据

`resample` 方法是改变时间序列数据频率的一种强大方式。在这里，我们将把当前的每小时时间序列数据聚合为每个测量站的每月最大值。

```python
# 通过透视数据，日期时间信息成为了表格的索引。
no_2 = air_quality.pivot(index="datetime", columns="location", values="value")
no_2.head()

# 创建一个从 5 月 20 日到 5 月 21 日结束的不同站点值的图表
no_2["2019-05-20":"2019-05-21"].plot()

# 重采样时间序列数据
monthly_max = no_2.resample("M").max()
monthly_max
```
