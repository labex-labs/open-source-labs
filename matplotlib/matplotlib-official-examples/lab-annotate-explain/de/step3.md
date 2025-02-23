# Ein Ellipsen zum Plot hinzufügen

In diesem Schritt fügen wir einem Plot eine Ellipse hinzu. Wir verwenden die `Ellipse`-Funktion, um die Ellipse zu erstellen und passen die Eigenschaften der Ellipse wie Position, Breite, Höhe und Winkel an.

```python
ax = axs.flat[1]
ax.plot([x1, x2], [y1, y2], ".")
el = mpatches.Ellipse((x1, y1), 0.3, 0.4, angle=30, alpha=0.2)
ax.add_artist(el)
```
