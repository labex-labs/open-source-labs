# 添加参数的完整描述和名称

最后，我们将把参数的完整描述和名称添加到测量数据表中。我们在 `parameter` 和 `id` 列上执行左连接。

```python
# 加载空气质量参数数据
air_quality_parameters = pd.read_csv("data/air_quality_parameters.csv")

# 合并 air_quality 和 air_quality_parameters 数据框
air_quality = pd.merge(air_quality, air_quality_parameters, how='left', left_on='parameter', right_on='id')
```
