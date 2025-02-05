# 鼠标移动时更新标签文本

当鼠标在坐标轴上拖动时，我们将更新标签文本以显示鼠标的 x、y 坐标。我们创建一个函数来更新标签文本，并使用 `mpl_connect()` 方法将其连接到 `motion_notify_event`。

```python
def update(event):
    if event.xdata is None:
        label.set_markup('Drag mouse over axes for position')
    else:
        label.set_markup(
            f'<span color="#ef0000">x,y=({event.xdata}, {event.ydata})</span>')

fig.canvas.mpl_connect('motion_notify_event', update)
```
