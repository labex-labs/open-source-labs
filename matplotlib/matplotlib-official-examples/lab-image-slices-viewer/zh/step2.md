# 创建数据

我们将使用 NumPy 的`ogrid`函数创建三维数据。

```python
x, y, z = np.ogrid[-10:10:100j, -10:10:100j, 1:10:20j]
X = np.sin(x * y * z) / (x * y * z)
```
