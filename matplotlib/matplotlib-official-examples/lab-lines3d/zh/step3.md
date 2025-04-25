# 定义 x、y 和 z 的值

我们将使用 NumPy 生成 x、y 和 z 的值。我们首先定义 theta 和 z 的值的范围。然后，我们将使用这些值来生成 r、x 和 y 的值。

```python
theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
z = np.linspace(-2, 2, 100)
r = z**2 + 1
x = r * np.sin(theta)
y = r * np.cos(theta)
```
