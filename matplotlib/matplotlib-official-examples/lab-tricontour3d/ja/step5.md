# 不要な三角形をマスクする

x 座標と y 座標の平均を使って、不要な三角形をマスクします。

```python
triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                         y[triang.triangles].mean(axis=1))
                < min_radius)
```
