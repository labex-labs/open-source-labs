# Définir les limites du tracé

Définissez les limites du tracé en utilisant la méthode `set` et en passant les limites des coordonnées X, Y et Z.

```python
# Définir les limites du tracé à partir des limites des coordonnées
xmin, xmax = X.min(), X.max()
ymin, ymax = Y.min(), Y.max()
zmin, zmax = Z.min(), Z.max()
ax.set(xlim=[xmin, xmax], ylim=[ymin, ymax], zlim=[zmin, zmax])
```
