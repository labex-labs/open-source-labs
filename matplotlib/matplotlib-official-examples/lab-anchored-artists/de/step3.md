# Füge verankerten Text hinzu

In diesem Schritt werden wir einen Textrahmen hinzufügen, der an der oberen linken Ecke der Figur befestigt ist.

```python
def draw_text(ax):
    """Zeichnet einen Textrahmen, der an der oberen linken Ecke der Figur befestigt ist."""
    box = AnchoredOffsetbox(child=TextArea("Figure 1a"),
                            loc="upper left", frameon=True)
    box.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
    ax.add_artist(box)

draw_text(ax)
```
