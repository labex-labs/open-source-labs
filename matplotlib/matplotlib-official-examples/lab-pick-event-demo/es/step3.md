# Selección en un diagrama de dispersión

Un diagrama de dispersión está respaldado por una `~matplotlib.collections.PathCollection`. Crearemos un diagrama de dispersión y habilitaremos la selección.

```python
x, y, c, s = rand(4, 100)


def onpick3(event):
    ind = event.ind
    print('onpick3 scatter:', ind, x[ind], y[ind])


fig, ax = plt.subplots()
ax.scatter(x, y, 100*s, c, picker=True)
fig.canvas.mpl_connect('pick_event', onpick3)
```
