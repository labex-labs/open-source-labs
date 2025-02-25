# Erstellen eines Teilplots

Wir werden einen Teilplot erstellen, um die gefärbten Liniensegmente anzuzeigen. Wir werden die `subplots`-Funktion aus `matplotlib.pyplot` verwenden, um ein 2x1-Gitter von Teilplots zu erstellen, und die Parameter `sharex` und `sharey`, um die x- und y-Achsen zwischen den Teilplots zu teilen.

```python
fig, axs = plt.subplots(2, 1, sharex=True, sharey=True)
line = axs[0].add_collection(lc)
fig.colorbar(line, ax=axs[0])
```
