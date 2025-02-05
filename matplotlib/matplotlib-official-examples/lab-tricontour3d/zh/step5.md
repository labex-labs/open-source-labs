# 屏蔽不需要的三角形

我们将使用 x 和 y 坐标的平均值来屏蔽不需要的三角形。

```python
triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                         y[triang.triangles].mean(axis=1))
                < min_radius)
```
