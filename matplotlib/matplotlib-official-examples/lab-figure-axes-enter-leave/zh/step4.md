# 将事件处理程序连接到图形画布

现在，我们将使用 `mpl_connect` 方法将事件处理程序连接到图形画布。这样，当鼠标进入或离开图形或坐标轴时，事件处理程序就会被触发。

```python
fig.canvas.mpl_connect('figure_enter_event', on_enter_figure)
fig.canvas.mpl_connect('figure_leave_event', on_leave_figure)
fig.canvas.mpl_connect('axes_enter_event', on_enter_axes)
fig.canvas.mpl_connect('axes_leave_event', on_leave_axes)
```
