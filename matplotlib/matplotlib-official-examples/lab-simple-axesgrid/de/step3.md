# Iterieren über das Gitter und Zeichnen der Bilder

Anschließend iterieren wir über das `grid`-Objekt mit der `zip`-Funktion, um sowohl über die Achsen als auch über die Bildarrays zu iterieren. Wir zeichnen jedes Bild auf seiner entsprechenden Achse mit der `imshow`-Funktion.

```python
for ax, im in zip(grid, [im1, im2, im3, im4]):
    ax.imshow(im)
```
