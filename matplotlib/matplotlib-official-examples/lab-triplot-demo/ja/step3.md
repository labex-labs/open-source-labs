# 不要な三角形をマスクする

各三角形の頂点の x 座標と y 座標の平均を計算し、それを最小半径と比較することで、不要な三角形をマスクします。

```python
triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                         y[triang.triangles].mean(axis=1))
                < min_radius)
```
