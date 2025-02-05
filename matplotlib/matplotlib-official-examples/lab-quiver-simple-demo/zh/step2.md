# 创建数据

我们需要使用 `np.meshgrid()` 函数创建 `X` 和 `Y` 坐标。然后，我们创建表示向量场的 `U` 和 `V` 数组。

```python
X = np.arange(-10, 10, 1)
Y = np.arange(-10, 10, 1)
U, V = np.meshgrid(X, Y)
```
