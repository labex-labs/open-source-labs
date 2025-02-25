# Подборка на точечной диаграмме

Точечная диаграмма основана на `~matplotlib.collections.PathCollection`. Мы создадим точечную диаграмму и применим подборку.

```python
x, y, c, s = rand(4, 100)


def onpick3(event):
    ind = event.ind
    print('onpick3 scatter:', ind, x[ind], y[ind])


fig, ax = plt.subplots()
ax.scatter(x, y, 100*s, c, picker=True)
fig.canvas.mpl_connect('pick_event', onpick3)
```
