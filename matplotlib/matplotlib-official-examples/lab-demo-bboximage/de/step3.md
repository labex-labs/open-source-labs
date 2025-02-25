# Erzeuge ein BboxImage für jede Farbskala

Als nächstes erzeugen wir ein BboxImage für jede Farbskala. Wir beginnen mit der Erstellung einer Liste aller Farbskalen mit der `plt.colormaps`-Methode. Anschließend erstellen wir eine `for`-Schleife, die durch die Liste der Farbskalen iteriert. Für jede Farbskala berechnen wir die `ix`- und `iy`-Position mit der `divmod()`-Methode. Danach erstellen wir ein `Bbox`-Objekt mit der `Bbox.from_bounds()`-Methode. Wir übergeben die `ix`, `iy`, `dx`- und `dy`-Werte an die `Bbox.from_bounds()`-Methode, um die Begrenzungsbox zu erstellen. Anschließend erstellen wir ein `TransformedBbox`-Objekt mit dem `Bbox`-Objekt und dem `ax2.transAxes`-Objekt. Schließlich erstellen wir ein `BboxImage`-Objekt mit der `add_artist()`-Methode. Wir übergeben das `TransformedBbox`-Objekt an den `BboxImage`-Konstruktor, um ein Bild mit der Farbskala zu erstellen.

```python
cmap_names = sorted(m for m in plt.colormaps if not m.endswith("_r"))

ncol = 2
nrow = len(cmap_names) // ncol + 1

xpad_fraction = 0.3
dx = 1 / (ncol + xpad_fraction * (ncol - 1))

ypad_fraction = 0.3
dy = 1 / (nrow + ypad_fraction * (nrow - 1))

for i, cmap_name in enumerate(cmap_names):
    ix, iy = divmod(i, nrow)
    bbox0 = Bbox.from_bounds(ix*dx*(1+xpad_fraction),
                             1 - iy*dy*(1+ypad_fraction) - dy,
                             dx, dy)
    bbox = TransformedBbox(bbox0, ax2.transAxes)
    ax2.add_artist(
        BboxImage(bbox, cmap=cmap_name, data=np.arange(256).reshape((1, -1))))
```
