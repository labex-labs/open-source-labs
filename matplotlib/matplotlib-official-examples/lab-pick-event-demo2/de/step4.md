# Interaktivität hinzufügen

Wenn auf einen Punkt im Punktwolkenplot geklickt wird, möchten wir die Rohdaten aus dem Datensatz plotten, der diesen Punkt erzeugt hat. Wir definieren eine Funktion `onpick`, die aufgerufen wird, wenn auf einen Punkt geklickt wird. Die Funktion wird die Rohdaten plotten und den Mittelwert und die Standardabweichung für diesen Datensatz anzeigen.

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
