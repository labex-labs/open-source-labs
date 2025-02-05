# 创建圆形

我们使用 `Circle()` 创建圆形，并将它们追加到一个补丁列表中。

```python
x = np.random.rand(N)
y = np.random.rand(N)
radii = 0.1*np.random.rand(N)
patches = []
for x1, y1, r in zip(x, y, radii):
    circle = Circle((x1, y1), r)
    patches.append(circle)
```
