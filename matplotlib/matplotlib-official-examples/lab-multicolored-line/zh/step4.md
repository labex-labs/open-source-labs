# 创建连续规范

我们将创建一个连续规范，用于将数据点映射到颜色。我们将使用 `matplotlib.pyplot` 中的 `Normalize` 函数，将 `dydx` 的值在其最小值和最大值之间进行归一化。然后，我们将使用 `LineCollection` 函数创建一组线段，并根据它们的导数分别为其着色。我们将使用 `set_array` 函数来设置用于颜色映射的值。

```python
norm = plt.Normalize(dydx.min(), dydx.max())
lc = LineCollection(segments, cmap='viridis', norm=norm)
lc.set_array(dydx)
lc.set_linewidth(2)
```
