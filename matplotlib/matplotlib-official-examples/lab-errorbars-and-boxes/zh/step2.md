# 准备数据

然后我们将为箱线图准备数据。我们将为x和y值以及误差值创建一些虚拟数据。

```python
# 数据点数量
n = 5

# 虚拟数据
np.random.seed(19680801)
x = np.arange(0, n, 1)
y = np.random.rand(n) * 5.

# 虚拟误差（上下）
xerr = np.random.rand(2, n) + 0.1
yerr = np.random.rand(2, n) + 0.2
```
