# Dessiner un cercle sur le mur

Nous allons dessiner un cercle sur le "mur" x = 0 du graphique 3D à l'aide des fonctions `Circle` et `pathpatch_2d_to_3d` de Matplotlib.

```python
p = Circle((5, 5), 3)
ax.add_patch(p)
art3d.pathpatch_2d_to_3d(p, z=0, zdir="x")
```
