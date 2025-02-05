# 创建多边形

我们使用 `Polygon()` 创建多边形，并将它们追加到补丁列表中。

```python
for i in range(N):
    polygon = Polygon(np.random.rand(N, 2), closed=True)
    patches.append(polygon)
```
