# 创建数据

接下来，我们将创建用于生成风羽图的数据。我们将使用`meshgrid`和乘法函数创建一个 5x5 的均匀网格和一个向量场。

```python
x = np.linspace(-5, 5, 5)
X, Y = np.meshgrid(x, x)
U, V = 12 * X, 12 * Y
```
