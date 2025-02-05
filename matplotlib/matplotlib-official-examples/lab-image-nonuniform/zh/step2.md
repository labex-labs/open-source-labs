# 创建线性和非线性数组

我们需要创建两个数组，一个包含线性值，另一个包含非线性值。这些数组将用于创建我们的 NonUniformImage。

```python
# 用于单元格中心的线性 x 数组：
x = np.linspace(-4, 4, 9)

# 高度非线性的 x 数组：
x2 = x**3

y = np.linspace(-4, 4, 9)

z = np.sqrt(x[np.newaxis, :]**2 + y[:, np.newaxis]**2)
```
