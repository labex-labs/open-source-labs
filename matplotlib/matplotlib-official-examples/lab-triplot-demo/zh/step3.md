# 屏蔽不需要的三角形

我们将通过计算每个三角形顶点的 x 和 y 坐标的平均值，并将其与最小半径进行比较，来屏蔽不需要的三角形。

```python
triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                         y[triang.triangles].mean(axis=1))
                < min_radius)
```
