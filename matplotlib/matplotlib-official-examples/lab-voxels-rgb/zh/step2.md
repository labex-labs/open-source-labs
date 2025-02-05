# 定义坐标和颜色

接下来，我们需要为图表定义坐标和颜色。在这个例子中，我们将使用 `np.indices` 函数来创建一个 17x17x17 的 RGB 颜色值网格。

```python
r, g, b = np.indices((17, 17, 17)) / 16.0
```

我们还将定义一个函数 `midpoints` 来找到网格中值之间的中点。这将在后面用于创建球体。

```python
def midpoints(x):
    sl = ()
    for _ in range(x.ndim):
        x = (x[sl + np.index_exp[:-1]] + x[sl + np.index_exp[1:]]) / 2.0
        sl += np.index_exp[:]
    return x
```
