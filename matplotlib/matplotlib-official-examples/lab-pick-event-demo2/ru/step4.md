# Добавление интерактивности

Когда на точечном графике кликается по какой - то точке, мы хотим построить исходные данные из набора данных, который сгенерировал эту точку. Мы определим функцию `onpick`, которая будет вызываться при нажатии на точку. Функция будет строить исходные данные и отображать среднее значение и стандартное отклонение для этого набора данных.

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
