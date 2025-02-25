# Definiere die Achsenpositionen mit inset_axes

Wir können auch `inset_axes` verwenden, um die Marginalien außerhalb der Hauptachsen zu positionieren. Der Vorteil dabei ist, dass das Seitenverhältnis der Hauptachsen fixiert werden kann und die Marginalien immer relativ zur Position der Achsen gezeichnet werden.

```python
# Erstelle eine Figur, die nicht quadratisch sein muss.
fig = plt.figure(layout='constrained')
# Erstelle die Hauptachsen, wobei 25% des Figurbereichs oben und rechts für die Positionierung von Marginalien frei gelassen werden.
ax = fig.add_gridspec(top=0.75, right=0.75).subplots()
# Das Seitenverhältnis der Hauptachsen kann fixiert werden.
ax.set(aspect=1)
# Erstelle Marginalachsen, die 25% der Größe der Hauptachsen haben.
# Beachten Sie, dass die inset-Achsen außerhalb (rechts und oben) der Hauptachsen positioniert werden,
# indem Achsenkoordinaten größer als 1 angegeben werden.
# Achsenkoordinaten kleiner als 0 würden ebenfalls Positionen links und unten der Hauptachsen angeben.
ax_histx = ax.inset_axes([0, 1.05, 1, 0.25], sharex=ax)
ax_histy = ax.inset_axes([1.05, 0, 0.25, 1], sharey=ax)
# Zeichne das Streudiagramm und die Marginalien.
scatter_hist(x, y, ax, ax_histx, ax_histy)
```
