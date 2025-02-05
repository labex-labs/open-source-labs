# 合并颜色

现在我们要将RGB颜色分量合并成一个形状为 `(17, 17, 17, 3)` 的单一数组。

```python
colors = np.zeros(sphere.shape + (3,))
colors[..., 0] = rc
colors[..., 1] = gc
colors[..., 2] = bc
```
