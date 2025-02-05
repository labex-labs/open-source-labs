# 创建掩码数组

在这一步中，我们将创建三个掩码数组：一个用于大于某个阈值的值，一个用于小于某个阈值的值，还有一个用于介于两个阈值之间的值。

```python
upper = 0.77
lower = -0.77

supper = np.ma.masked_where(s < upper, s)
slower = np.ma.masked_where(s > lower, s)
smiddle = np.ma.masked_where((s < lower) | (s > upper), s)
```
