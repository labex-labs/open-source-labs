# Ajouter de l'interactivité

Lorsque l'on clique sur un point du graphique en points à dispersion, on souhaite tracer les données brutes du jeu de données qui a généré ce point. Nous allons définir une fonction `onpick` qui sera appelée lorsqu'un point est cliqué. La fonction dessinera les données brutes et affichera la moyenne et l'écart-type pour ce jeu de données.

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
