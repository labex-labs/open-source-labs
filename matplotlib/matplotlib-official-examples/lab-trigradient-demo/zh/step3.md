# 创建三角剖分

```python
triang = Triangulation(x, y)

triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                         y[triang.triangles].mean(axis=1))
                < min_radius)
```

解释：

- `Triangulation` 是一个从一组点创建德劳内三角剖分的类。
- `triang` 是 `Triangulation` 类的一个实例。
- `triang.set_mask` 会屏蔽掉不需要的三角形。
