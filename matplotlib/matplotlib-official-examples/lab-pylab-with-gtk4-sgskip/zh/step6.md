# 使用光标坐标更新标签

```python
def update(event):
    if event.xdata is None:
        label.set_markup('Drag mouse over axes for position')
    else:
        label.set_markup(
            f'<span color="#ef0000">x,y=({event.xdata}, {event.ydata})</span>')

fig.canvas.mpl_connect('motion_notify_event', update)
```

我们创建了一个函数，当光标在绘图区域上移动时，该函数会使用光标的x和y坐标来更新标签。我们将该函数连接到画布的 `motion_notify_event`。
