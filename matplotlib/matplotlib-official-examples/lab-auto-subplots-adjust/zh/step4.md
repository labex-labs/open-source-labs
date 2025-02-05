# 将绘制事件连接到回调函数

我们需要将 `draw_event` 连接到我们的 `on_draw` 函数。

```python
fig.canvas.mpl_connect('draw_event', on_draw)
```
