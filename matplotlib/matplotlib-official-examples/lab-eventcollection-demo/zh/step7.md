# 将事件添加到图表中

我们将使用 `matplotlib.pyplot.add_collection()` 函数把这些事件添加到图表中。

```python
# add the events to the axis
ax.add_collection(xevents1)
ax.add_collection(xevents2)
ax.add_collection(yevents1)
ax.add_collection(yevents2)
```
