# カスタム三角分割の作成

このステップでは、カスタム三角分割を作成し、不要な三角形をマスクします。

```python
triang = tri.Triangulation(x, y)
triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                         y[triang.triangles].mean(axis=1))
                < min_radius)
```
