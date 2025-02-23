# Füge verankerte Kreise hinzu

In diesem Schritt werden wir zwei Kreise zum Graphen hinzufügen, indem wir verankerte Objekte verwenden.

```python
def draw_circles(ax):
    """Zeichnet Kreise in Koordinaten der Achsen."""
    area = DrawingArea(width=40, height=20)
    area.add_artist(Circle((10, 10), 10, fc="tab:blue"))
    area.add_artist(Circle((30, 10), 5, fc="tab:red"))
    box = AnchoredOffsetbox(
        child=area, loc="upper right", pad=0, frameon=False)
    ax.add_artist(box)

draw_circles(ax)
```
