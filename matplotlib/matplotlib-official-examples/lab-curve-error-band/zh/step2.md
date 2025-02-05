# 定义曲线

接下来，我们定义要在其周围绘制误差带的曲线。在本示例中，我们将使用参数化曲线。参数化曲线 x(t)，y(t) 可以直接使用 `~.Axes.plot` 绘制。

```python
N = 400
t = np.linspace(0, 2 * np.pi, N)
r = 0.5 + np.cos(t)
x, y = r * np.cos(t), r * np.sin(t)
```
