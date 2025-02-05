# 设置交互性

我们需要设置交互性来更新光标下方的三角形。我们将使用 `motion_notify_event` 来检测鼠标何时在绘图区域上移动。我们将创建一个函数 `on_mouse_move()`，该函数将使用 TriFinder 对象获取光标下方的三角形，用三角形的顶点更新多边形，并使用三角形的索引更新绘图标题。

```python
def on_mouse_move(event):
    if event.inaxes is None:
        tri = -1
    else:
        tri = trifinder(event.xdata, event.ydata)
    update_polygon(tri)
    ax.set_title(f'Triangle {tri}')
    event.canvas.draw()

fig.canvas.mpl_connect('motion_notify_event', on_mouse_move)
```
