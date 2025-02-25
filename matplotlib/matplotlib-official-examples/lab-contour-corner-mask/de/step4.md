# Erstellen des Plots

In diesem Schritt werden wir den maskierten Konturplot mit der Funktion `contourf()` erstellen. Wir übergeben die `x`, `y` und `z`-Arrays an diese Funktion, zusammen mit dem Argument `corner_mask`, das auf `True` oder `False` gesetzt wird, je nachdem, welchen Plottyp wir erstellen möchten.

```python
corner_masks = [False, True]
fig, axs = plt.subplots(ncols=2)
for ax, corner_mask in zip(axs, corner_masks):
    cs = ax.contourf(x, y, z, corner_mask=corner_mask)
    ax.contour(cs, colors='k')
    ax.set_title(f'{corner_mask=}')

    # Plot grid.
    ax.grid(c='k', ls='-', alpha=0.3)

    # Indicate masked points with red circles.
    ax.plot(np.ma.array(x, mask=~mask), y, 'ro')

plt.show()
```
