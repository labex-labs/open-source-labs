# Utiliser une norme de limite

Au lieu de cela, nous allons utiliser une norme de limite pour colorer les segments de ligne. Nous allons créer une `ListedColormap` contenant trois couleurs - rouge, verte et bleue. Nous allons ensuite créer une `BoundaryNorm` avec des limites -1, -0,5, 0,5 et 1, et la `ListedColormap`. Nous utiliserons la fonction `set_array` pour définir les valeurs utilisées pour la cartographie des couleurs.

```python
cmap = ListedColormap(['r', 'g', 'b'])
norm = BoundaryNorm([-1, -0.5, 0.5, 1], cmap.N)
lc = LineCollection(segments, cmap=cmap, norm=norm)
lc.set_array(dydx)
lc.set_linewidth(2)
```
