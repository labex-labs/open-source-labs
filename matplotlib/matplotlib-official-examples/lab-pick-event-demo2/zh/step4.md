# 添加交互性

当点击散点图上的一个点时，我们希望绘制生成该点的数据集的原始数据。我们将定义一个函数 `onpick`，当点击一个点时该函数会被调用。这个函数将绘制原始数据，并显示该数据集的均值和标准差。

```python
def onpick(event):

    if event.artist!= line:
        return

    N = len(event.ind)
    if not N:
        return

    figi, axs = plt.subplots(N, squeeze=False)
    for ax, dataind in zip(axs.flat, event.ind):
        ax.plot(X[dataind])
        ax.text(.05,.9, f'mu={xs[dataind]:1.3f}\nsigma={ys[dataind]:1.3f}',
                transform=ax.transAxes, va='top')
        ax.set_ylim(-0.5, 1.5)
    figi.show()


fig.canvas.mpl_connect('pick_event', onpick)
```
