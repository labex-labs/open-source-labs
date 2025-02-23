# Ajouter des cercles ancrés

Dans cette étape, nous allons ajouter deux cercles au graphique en utilisant des Objets Ancrés.

```python
def draw_circles(ax):
    """Draw circles in axes coordinates."""
    area = DrawingArea(width=40, height=20)
    area.add_artist(Circle((10, 10), 10, fc="tab:blue"))
    area.add_artist(Circle((30, 10), 5, fc="tab:red"))
    box = AnchoredOffsetbox(
        child=area, loc="upper right", pad=0, frameon=False)
    ax.add_artist(box)

draw_circles(ax)
```
