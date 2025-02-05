# 创建线段

我们将创建一组线段，以便能够分别为它们上色。我们将使用NumPy的 `concatenate` 函数，沿着第二个轴连接两个数组 `points[:-1]` 和 `points[1:]`。然后，我们会将结果数组重塑为一个N x 1 x 2的数组，这样我们就可以轻松地将点堆叠在一起以获得线段。用于线集合的线段数组需要是 (线段数量) x (每条线段的点数) x 2（用于x和y）。

```python
points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
```
