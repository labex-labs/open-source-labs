# 加载数据集

我们将加载两个与空气质量相关的数据集。一个包含硝酸盐数据，另一个包含颗粒物数据。

```python
# 加载硝酸盐数据
air_quality_no2 = pd.read_csv("data/air_quality_no2_long.csv", parse_dates=True)
air_quality_no2 = air_quality_no2[["date.utc", "location", "parameter", "value"]]

# 加载颗粒物数据
air_quality_pm25 = pd.read_csv("data/air_quality_pm25_long.csv", parse_dates=True)
air_quality_pm25 = air_quality_pm25[["date.utc", "location", "parameter", "value"]]
```
