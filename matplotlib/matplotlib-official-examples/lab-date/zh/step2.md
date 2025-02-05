# 加载数据

接下来，我们将加载想要绘制的数据。我们将使用来自雅虎 csv 数据的 numpy 记录数组，其字段包括日期、开盘价、最高价、最低价、收盘价、成交量、调整收盘价，数据来自 mpl-data/sample_data 目录。记录数组在日期列中将日期存储为具有日单位（'D'）的 np.datetime64。

```python
data = cbook.get_sample_data('goog.npz')['price_data']
```
