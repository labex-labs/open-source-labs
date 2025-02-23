# Ajouter une ellipse ancrée

Dans cette étape, nous allons ajouter une ellipse au graphique en utilisant des Objets Ancrés.

```python
def draw_ellipse(ax):
    """Draw an ellipse of width=0.1, height=0.15 in data coordinates."""
    aux_tr_box = AuxTransformBox(ax.transData)
    aux_tr_box.add_artist(Ellipse((0, 0), width=0.1, height=0.15))
    box = AnchoredOffsetbox(child=aux_tr_box, loc="lower left", frameon=True)
    ax.add_artist(box)

draw_ellipse(ax)
```
