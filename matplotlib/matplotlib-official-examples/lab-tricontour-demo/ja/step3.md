# 不要な三角形をマスクする

不要な三角形をマスクするために、`set_mask` メソッドを使用します。

```python
triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                         y[triang.triangles].mean(axis=1))
                < min_radius)
```
