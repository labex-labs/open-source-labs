# Füge Maßstab hinzu

In diesem Schritt werden wir einen Maßstab zum Graphen hinzufügen, indem wir verankerte Objekte verwenden.

```python
def draw_sizebar(ax):
    """
    Zeichnet eine horizontale Linie mit einer Länge von 0,1 in Datenkoordinaten,
    mit einem festen, mittig ausgerichteten Label darunter.
    """
    size = 0.1
    text = r"1$^{\prime}$"
    sizebar = AuxTransformBox(ax.transData)
    sizebar.add_artist(Line2D([0, size], [0, 0], color="black"))
    text = TextArea(text)
    packer = VPacker(
        children=[sizebar, text], align="center", sep=5)  # Abstand in Punkten.
    ax.add_artist(AnchoredOffsetbox(
        child=packer, loc="lower center", frameon=False,
        pad=0.1, borderpad=0.5))  # Paddings relativ zur Legenden-Schriftgröße.

draw_sizebar(ax)
```
