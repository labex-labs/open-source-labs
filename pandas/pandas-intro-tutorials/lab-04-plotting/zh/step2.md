# 加载数据

本教程我们将使用空气质量数据。数据将从 CSV 文件加载到 Pandas DataFrame 中。

```python
# 加载数据
air_quality = pd.read_csv("data/air_quality_no2.csv", index_col=0, parse_dates=True)
air_quality.head()
```
