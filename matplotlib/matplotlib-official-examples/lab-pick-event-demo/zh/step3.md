# 在散点图上进行拾取

散点图由 `~matplotlib.collections.PathCollection` 支持。我们将创建一个散点图并启用拾取功能。

```python
x, y, c, s = rand(4, 100)


def onpick3(event):
    ind = event.ind
    print('onpick3 scatter:', ind, x[ind], y[ind])


fig, ax = plt.subplots()
ax.scatter(x, y, 100*s, c, picker=True)
fig.canvas.mpl_connect('pick_event', onpick3)
```
