# 定义箭头方向

现在我们将定义箭头的方向。在本示例中，我们将使用 NumPy 的三角函数来定义箭头的方向。`sin` 和 `cos` 函数用于创建 `u`、`v` 和 `w` 数组，这些数组表示箭头在 `x`、`y` 和 `z` 方向上的方向。

```python
u = np.sin(np.pi * x) * np.cos(np.pi * y) * np.cos(np.pi * z)
v = -np.cos(np.pi * x) * np.sin(np.pi * y) * np.cos(np.pi * z)
w = (np.sqrt(2.0 / 3.0) * np.cos(np.pi * x) * np.cos(np.pi * y) *
     np.sin(np.pi * z))
```
