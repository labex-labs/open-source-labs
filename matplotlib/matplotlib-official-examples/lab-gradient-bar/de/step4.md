# Definieren der Gradientenbalkenfunktion

Als nächstes müssen wir eine Funktion definieren, die einen Gradientenbalken erstellt. Diese Funktion wird das Achsenobjekt, die x- und y-Koordinaten des Balkens, die Breite des Balkens und die untere Position des Balkens entgegennehmen. Die Funktion wird dann für jeden Balken ein Gradientenbild erstellen und zurückgeben.

```python
def gradient_bar(ax, x, y, width=0.5, bottom=0):
    for left, top in zip(x, y):
        right = left + width
        gradient_image(ax, extent=(left, right, bottom, top),
                       cmap=plt.cm.Blues_r, cmap_range=(0, 0.8))
```
