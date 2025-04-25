# 创建绘图并连接滚动事件

我们将使用 Matplotlib 的`subplots`函数创建绘图，并将创建的`IndexTracker`对象传递给它。然后，我们将使用`mpl_connect`将滚动事件连接到图形画布。

```python
fig, ax = plt.subplots()
tracker = IndexTracker(ax, X)

fig.canvas.mpl_connect('scroll_event', tracker.on_scroll)
plt.show()
```
