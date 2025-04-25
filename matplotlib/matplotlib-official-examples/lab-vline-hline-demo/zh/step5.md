# 添加垂直线

在这一步中，我们将向绘图中添加垂直线。我们将使用 Matplotlib 的`vlines`函数来绘制垂直线。我们还将使用`transform`参数将 y 坐标设置为从 0 到 1 进行缩放。我们将在 x = 1 和 x = 2 处绘制两条垂直线。

```python
# 添加垂直线
vax.plot(t, s + nse, '^')
vax.vlines(t, [0], s)
vax.vlines([1, 2], 0, 1, transform=vax.get_xaxis_transform(), colors='r')
vax.set_xlabel('time (s)')
vax.set_title('Vertical lines demo')
```
