# Fügen eines Einzugsdiagramms hinzu

In diesem Schritt werden wir einem Hauptdiagramm ein Einzugsdiagramm hinzufügen. Dieses Einzugsdiagramm wird einen vergrößerten Bereich des Hauptdiagramms anzeigen.

```python
# inset axes....
x1, x2, y1, y2 = -1.5, -0.9, -2.5, -1.9  # subregion of the original image
axins = ax.inset_axes(
    [0.5, 0.5, 0.47, 0.47],
    xlim=(x1, x2), ylim=(y1, y2), xticklabels=[], yticklabels=[])
axins.imshow(Z2, extent=extent, origin="lower")
```
