# 不要な三角形をマスクする

各三角形の中点を計算し、与えられた半径内にあるかどうかをチェックすることで、不要な三角形をマスクします。

```python
xmid = x[triang.triangles].mean(axis=1)
ymid = y[triang.triangles].mean(axis=1)
mask = xmid**2 + ymid**2 < min_radius**2
triang.set_mask(mask)
```
