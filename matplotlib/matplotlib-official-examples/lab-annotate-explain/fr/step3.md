# Ajouter une ellipse au graphique

Dans cette étape, nous allons ajouter une ellipse au graphique. Nous utiliserons la fonction `Ellipse` pour créer l'ellipse et personnaliser les propriétés de l'ellipse telles que la position, la largeur, la hauteur et l'angle.

```python
ax = axs.flat[1]
ax.plot([x1, x2], [y1, y2], ".")
el = mpatches.Ellipse((x1, y1), 0.3, 0.4, angle=30, alpha=0.2)
ax.add_artist(el)
```
