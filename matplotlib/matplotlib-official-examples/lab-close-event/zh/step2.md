# 创建一个图形并连接关闭事件

在这一步中，我们将创建一个图形，并将关闭事件连接到第一步中定义的 `on_close` 函数。这是通过图形画布的 `mpl_connect` 方法完成的。

```python
fig = plt.figure()
fig.canvas.mpl_connect('close_event', on_close)
```
