# 屏蔽不需要的三角形

我们通过计算每个三角形的中点并检查其是否落在给定半径内来屏蔽不需要的三角形。

```python
xmid = x[triang.triangles].mean(axis=1)
ymid = y[triang.triangles].mean(axis=1)
mask = xmid**2 + ymid**2 < min_radius**2
triang.set_mask(mask)
```
