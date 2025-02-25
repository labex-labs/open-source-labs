# 三角分割を作成する

```python
triang = Triangulation(x, y)

triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                         y[triang.triangles].mean(axis=1))
                < min_radius)
```

解説:

- `Triangulation`は一連の点からデロネ三角分割を作成するクラスです。
- `triang`は`Triangulation`クラスのインスタンスです。
- `triang.set_mask`は不要な三角形をマスクします。
