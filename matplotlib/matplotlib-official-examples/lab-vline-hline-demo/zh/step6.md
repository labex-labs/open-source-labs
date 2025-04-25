# 添加水平线

在这一步中，我们将向绘图中添加水平线。我们将使用 Matplotlib 的`hlines`函数来绘制水平线。我们将在 y = 0.5、y = 2.5 和 y = 4.5 处绘制水平线。

```python
# 添加水平线
hax.plot(s + nse, t, '^')
hax.hlines(t, [0], s, lw=2)
hax.set_xlabel('time (s)')
hax.set_title('Horizontal lines demo')
```
