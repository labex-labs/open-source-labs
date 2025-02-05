# 计算散点图所需的值

我们将计算用于散点图的delta1、成交量和收盘价的值。

```python
delta1 = np.diff(price_data.adj_close) / price_data.adj_close[:-1]

# 标记大小，单位为点^2
volume = (15 * price_data.volume[:-2] / price_data.volume[0])**2
close = 0.003 * price_data.close[:-2] / 0.003 * price_data.open[:-2]
```
