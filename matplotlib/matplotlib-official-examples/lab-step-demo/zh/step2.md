# 创建绘图数据

接下来，让我们创建一些用于绘图的数据。我们将使用 `numpy.arange()` 函数创建一个从 0 到 14 的值数组，并将其存储在变量 `x` 中。我们还将使用 `numpy.sin()` 函数创建一个数组，该数组的值是 `x` 中每个值除以 2 后的正弦值，并将其存储在变量 `y` 中。

```python
x = np.arange(14)
y = np.sin(x / 2)
```
