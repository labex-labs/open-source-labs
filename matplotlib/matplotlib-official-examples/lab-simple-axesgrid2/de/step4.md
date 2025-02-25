# Anzeigen von Bildern im ImageGrid

Schließlich zeigen wir die Bilder im ImageGrid mit der Funktion `imshow` und der Funktion `zip`, um durch die Achsen im Gitter zu iterieren.

```python
for ax, im in zip(grid, [im1, im2, im3]):
    ax.imshow(im, origin="lower", vmin=vmin, vmax=vmax)

plt.show()
```
