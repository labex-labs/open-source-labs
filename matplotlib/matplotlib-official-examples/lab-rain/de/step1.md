# Erstellen einer neuen Figur und Achse

Der erste Schritt besteht darin, eine neue Figur und eine Achse zu erstellen, die diese ausfüllt. Dies wird die Leinwand sein, auf der die Simulation gezeichnet wird.

```python
fig = plt.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1], frameon=False)
ax.set_xlim(0, 1), ax.set_xticks([])
ax.set_ylim(0, 1), ax.set_yticks([])
```
