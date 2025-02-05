# 为绘图创建数据

为绘图创建一些数据。在这个例子中，我们将使用 `numpy` 库创建 `x` 和 `y` 数组。

```python
x = np.linspace(-3, 3, 201)
y = np.tanh(x) + 0.1 * np.cos(5 * x)
```
