# Seleção em um Gráfico de Dispersão (Scatter Plot)

Um gráfico de dispersão é suportado por um `~matplotlib.collections.PathCollection`. Criaremos um gráfico de dispersão e habilitaremos a seleção.

```python
x, y, c, s = rand(4, 100)


def onpick3(event):
    ind = event.ind
    print('onpick3 scatter:', ind, x[ind], y[ind])


fig, ax = plt.subplots()
ax.scatter(x, y, 100*s, c, picker=True)
fig.canvas.mpl_connect('pick_event', onpick3)
```
