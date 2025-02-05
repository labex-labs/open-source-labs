# 使用公共标识符合并表格

然后，我们将使用 `merge` 函数把站点坐标添加到测量数据表中。我们将在 `location` 列上执行左连接。

```python
# 加载站点坐标数据
stations_coord = pd.read_csv("data/air_quality_stations.csv")

# 合并 air_quality 和 stations_coord 数据框
air_quality = pd.merge(air_quality, stations_coord, how="left", on="location")
```
