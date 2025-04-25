# 加载数据

我们将从 mpl-data/sample_data 目录中加载一个来自雅虎 csv 数据的 numpy 记录数组，其字段包括日期、开盘价、最高价、最低价、收盘价、成交量、调整收盘价。记录数组在日期列中将日期存储为具有日单位（'D'）的 np.datetime64。

```python
import matplotlib.cbook as cbook

price_data = cbook.get_sample_data('goog.npz')['price_data'].view(np.recarray)
price_data = price_data[-250:]  # 获取最近 250 个交易日的数据
```
