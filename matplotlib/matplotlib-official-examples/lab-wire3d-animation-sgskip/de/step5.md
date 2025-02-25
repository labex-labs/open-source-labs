# Den Graphen animieren

Der fünfte Schritt besteht darin, den Graphen zu animieren. Wir werden eine for-Schleife verwenden, um durch einen Wertebereich für phi zu iterieren. In jeder Iteration werden wir die vorherige Linienmenge entfernen, neue Daten generieren, das neue Drahtgitter plotten und kurz pausieren, bevor wir fortfahren.

```python
wframe = None
tstart = time.time()
for phi in np.linspace(0, 180. / np.pi, 100):
    if wframe:
        wframe.remove()
    Z = np.cos(2 * np.pi * X + phi) * (1 - np.hypot(X, Y))
    wframe = ax.plot_wireframe(X, Y, Z, rstride=2, cstride=2)
    plt.pause(.001)
```
