# 生成数据

在这一步中，我们将生成折线图的数据。我们将使用 NumPy 的 `arange()` 函数生成 x 轴的值数组，并使用 `sin()` 函数生成正弦波的 y 轴值数组。

```python
x = np.arange(0, 2*np.pi, 0.01)
line, = ax.plot(x, np.sin(x))
```
