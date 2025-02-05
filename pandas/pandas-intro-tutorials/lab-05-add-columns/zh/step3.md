# 检查两列值的比率

接下来，我们将检查“station_paris”和“station_antwerp”列中值的比率，并将结果保存在一个新列中。

```python
# 通过用“station_paris”除以“station_antwerp”来创建新列
air_quality["ratio_paris_antwerp"] = air_quality["station_paris"] / air_quality["station_antwerp"]
```
