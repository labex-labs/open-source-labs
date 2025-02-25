# Ajoutez un graphique inséré

Dans cette étape, nous allons ajouter un graphique inséré au graphique principal. Ce graphique inséré montrera une région agrandie du graphique principal.

```python
# inset axes....
x1, x2, y1, y2 = -1.5, -0.9, -2.5, -1.9  # sous-région de l'image d'origine
axins = ax.inset_axes(
    [0.5, 0.5, 0.47, 0.47],
    xlim=(x1, x2), ylim=(y1, y2), xticklabels=[], yticklabels=[])
axins.imshow(Z2, extent=extent, origin="lower")
```
