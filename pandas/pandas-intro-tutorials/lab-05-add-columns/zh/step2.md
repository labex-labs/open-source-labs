# 创建新列

我们将通过把“station_london”列乘以一个转换因子来创建一个新列“london_mg_per_cubic”。

```python
# 通过将“station_london”乘以转换因子来创建新列
air_quality["london_mg_per_cubic"] = air_quality["station_london"] * 1.882
```
