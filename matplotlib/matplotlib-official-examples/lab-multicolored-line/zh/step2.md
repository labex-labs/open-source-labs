# 创建数据

我们将创建一个 NumPy 数组 `x`，它包含在 0 到 3π之间均匀分布的 500 个值。我们还将创建另一个 NumPy 数组 `y`，它包含 `x` 中值的正弦值。最后，我们将创建一个 NumPy 数组 `dydx`，它包含 `y` 的一阶导数。

```python
x = np.linspace(0, 3 * np.pi, 500)
y = np.sin(x)
dydx = np.cos(0.5 * (x[:-1] + x[1:]))
```
