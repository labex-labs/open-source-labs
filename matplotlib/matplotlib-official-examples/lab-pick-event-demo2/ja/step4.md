# インタラクティビティの追加

散布図上の点がクリックされたとき、その点を生成したデータセットの元のデータをプロットしたいと思います。点がクリックされたときに呼び出される`onpick`という関数を定義します。この関数は、元のデータをプロットし、そのデータセットの平均と標準偏差を表示します。

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
