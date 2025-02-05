# 创建表面图的数据

在这一步中，我们将创建表面图的数据。我们将创建 X 和 Y 值的网格，计算径向距离 R，并使用 `np.sin()` 根据 R 值计算 Z 值。

```python
# 创建表面图的数据
X = np.arange(-5, 5, 0.25)
xlen = len(X)
Y = np.arange(-5, 5, 0.25)
ylen = len(Y)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
```
