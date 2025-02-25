# Agregar interactividad

Cuando se hace clic en un punto del diagrama de dispersión, queremos graficar los datos crudos del conjunto de datos que generó ese punto. Definiremos una función `onpick` que se llamará cuando se haga clic en un punto. La función graficará los datos crudos y mostrará la media y la desviación estándar para ese conjunto de datos.

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
