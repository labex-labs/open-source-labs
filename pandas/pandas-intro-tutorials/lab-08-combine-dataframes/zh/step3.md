# 拼接数据集

接下来，我们将使用 `concat` 函数把硝酸盐和颗粒物的测量数据合并到一个表格中。

```python
# 拼接两个数据框
air_quality = pd.concat([air_quality_pm25, air_quality_no2], axis=0)
```
