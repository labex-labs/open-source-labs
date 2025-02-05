# 向图形添加线条

我们可以使用 `fig.add_artist()` 方法向图形添加线条。我们将创建两条线 —— 一条从 (0,0) 到 (1,1)，另一条从 (0,1) 到 (1,0)。

```python
fig.add_artist(lines.Line2D([0, 1], [0, 1]))
fig.add_artist(lines.Line2D([0, 1], [1, 0]))
```
