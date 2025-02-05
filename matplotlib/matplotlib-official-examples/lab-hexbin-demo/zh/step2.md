# 生成数据

我们将使用 `numpy.random.standard_normal()` 生成 100,000 个数据点。`standard_normal()` 从均值为 0、标准差为 1 的标准正态分布中生成随机数。

```python
np.random.seed(19680801)

n = 100_000
x = np.random.standard_normal(n)
y = 2.0 + 3.0 * x + 4.0 * np.random.standard_normal(n)
xlim = x.min(), x.max()
ylim = y.min(), y.max()
```
