# 创建自定义命中测试函数

在这一步中，我们将通过将 `picker` 设置为一个可调用函数来定义一个自定义拾取器。该函数将确定艺术家对象是否被鼠标事件命中。如果鼠标事件发生在艺术家对象上方，我们将返回 `hit=True`，并且 `props` 是一个字典，其中包含你想要添加到 `.PickEvent` 属性中的属性。

```python
def line_picker(line, mouseevent):
    """
    在数据坐标中找到距离鼠标点击一定距离内的点，并附加一些额外的属性，pickx 和 picky，
    它们是被拾取的数据点。
    """
    if mouseevent.xdata is None:
        return False, dict()
    xdata = line.get_xdata()
    ydata = line.get_ydata()
    maxd = 0.05
    d = np.sqrt(
        (xdata - mouseevent.xdata)**2 + (ydata - mouseevent.ydata)**2)

    ind, = np.nonzero(d <= maxd)
    if len(ind):
        pickx = xdata[ind]
        picky = ydata[ind]
        props = dict(ind=ind, pickx=pickx, picky=picky)
        return True, props
    else:
        return False, dict()


def onpick2(event):
    print('onpick2 line:', event.pickx, event.picky)


fig, ax = plt.subplots()
ax.set_title('custom picker for line data')
line, = ax.plot(rand(100), rand(100), 'o', picker=line_picker)
fig.canvas.mpl_connect('pick_event', onpick2)
```
