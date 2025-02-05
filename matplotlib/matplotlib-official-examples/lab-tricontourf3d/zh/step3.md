# 创建自定义三角剖分

在这一步中，我们将创建一个自定义三角剖分，并屏蔽掉不需要的三角形。

```python
triang = tri.Triangulation(x, y)
triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                         y[triang.triangles].mean(axis=1))
                < min_radius)
```
