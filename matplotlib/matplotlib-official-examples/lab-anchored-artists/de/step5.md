# Füge verankertes Ellips hinzu

In diesem Schritt werden wir eine Ellipse zum Graphen hinzufügen, indem wir verankerte Objekte verwenden.

```python
def draw_ellipse(ax):
    """Zeichnet eine Ellipse mit Breite = 0,1 und Höhe = 0,15 in Datenkoordinaten."""
    aux_tr_box = AuxTransformBox(ax.transData)
    aux_tr_box.add_artist(Ellipse((0, 0), width=0.1, height=0.15))
    box = AnchoredOffsetbox(child=aux_tr_box, loc="lower left", frameon=True)
    ax.add_artist(box)

draw_ellipse(ax)
```
