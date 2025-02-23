# Ajouter du texte ancré

Dans cette étape, nous allons ajouter une boîte de texte ancrée dans le coin supérieur gauche de la figure.

```python
def draw_text(ax):
    """Draw a text-box anchored to the upper-left corner of the figure."""
    box = AnchoredOffsetbox(child=TextArea("Figure 1a"),
                            loc="upper left", frameon=True)
    box.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
    ax.add_artist(box)

draw_text(ax)
```
