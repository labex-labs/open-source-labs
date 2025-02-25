# Erzeuge ein BboxImage mit Text

Wir beginnen mit der Erzeugung eines BboxImage mit Text. Wir erstellen ein `text`-Objekt mit der `text()`-Methode und fügen es dem `ax1`-Objekt hinzu. Anschließend erstellen wir ein `BboxImage`-Objekt mit der `add_artist()`-Methode. Wir übergeben die `get_window_extent`-Methode des `text`-Objekts an den `BboxImage`-Konstruktor, um die Begrenzungsbox für den Text zu erhalten. Wir übergeben auch ein eindimensionales Array der Form (1, 256) an den `data`-Parameter des `BboxImage`-Konstruktors, um ein Bild zu erstellen.

```python
fig, (ax1, ax2) = plt.subplots(ncols=2)

txt = ax1.text(0.5, 0.5, "test", size=30, ha="center", color="w")
ax1.add_artist(
    BboxImage(txt.get_window_extent, data=np.arange(256).reshape((1, -1))))
```
