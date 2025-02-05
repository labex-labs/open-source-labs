# 将拾取事件函数连接到画布

我们将把拾取事件函数连接到画布上。

```python
fig.canvas.mpl_connect('pick_event', on_pick)
```
