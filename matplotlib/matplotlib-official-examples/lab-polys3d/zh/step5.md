# 计算顶点和面颜色

我们使用 Matplotlib 的 `vectorize` 和 `colormaps` 函数来计算顶点和面颜色。

```python
# verts[i] 是定义多边形 i 的 (x, y) 对列表。
gamma = np.vectorize(math.gamma)
verts = [polygon_under_graph(x, l**x * np.exp(-l) / gamma(x + 1))
         for l in lambdas]
facecolors = plt.colormaps['viridis_r'](np.linspace(0, 1, len(verts)))
```
