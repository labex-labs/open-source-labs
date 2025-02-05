# 计算一周中每天的平均二氧化氮浓度

现在我们可以计算每个测量地点一周中每天的平均二氧化氮浓度。这可以使用 `groupby` 方法来完成。

```python
# 计算一周中每天的平均二氧化氮浓度
average_NO2 = air_quality.groupby([air_quality["datetime"].dt.weekday, "location"])["value"].mean()
```
