# 准备坐标

接下来，我们将为体素图准备坐标。我们将使用 NumPy 的 `indices` 函数创建一个 8x8x8 的点网格。

```python
x, y, z = np.indices((8, 8, 8))
```
