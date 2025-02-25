# Innere Gitter und Teilplots erstellen

In diesem Schritt werden wir die inneren Gitter und Teilplots mit verschachtelten `.GridSpec`s erstellen. Wir werden durch jede Zelle im äußeren Gitter iterieren und für jede Zelle ein 3x3-Gitter erstellen.

```python
for a in range(4):
    for b in range(4):
        # Gitter innerhalb eines Gitters
        inner_grid = outer_grid[a, b].subgridspec(3, 3, wspace=0, hspace=0)
        axs = inner_grid.subplots()  # Erstellt alle Teilplots für das innere Gitter.
        for (c, d), ax in np.ndenumerate(axs):
            ax.plot(*squiggle_xy(a + 1, b + 1, c + 1, d + 1))
            ax.set(xticks=[], yticks=[])
```
