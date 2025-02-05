# 定义x、y和z的值

我们将使用NumPy生成x、y和z的值。我们首先定义theta和z的值的范围。然后，我们将使用这些值来生成r、x和y的值。

```python
theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
z = np.linspace(-2, 2, 100)
r = z**2 + 1
x = r * np.sin(theta)
y = r * np.cos(theta)
```
