# Créez la fonction hatches_plot

La fonction hatches_plot créera un rectangle avec le motif de hachure spécifié et l'ajoutera à l'axe. Elle ajoutera également un texte avec le motif de hachure.

```python
def hatches_plot(ax, h):
    ax.add_patch(Rectangle((0, 0), 2, 2, fill=False, hatch=h))
    ax.text(1, -0.5, f"' {h} '", size=15, ha="center")
    ax.axis('equal')
    ax.axis('off')
```
