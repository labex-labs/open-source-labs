# Création des sommets et des codes

Nous allons créer les sommets et les codes pour les deux polygones que nous voulons combiner en un chemin composé. Nous utiliserons `Path.MOVETO` pour déplacer le curseur au point de départ du polygone, `Path.LINETO` pour créer une ligne du point de départ au point suivant et `Path.CLOSEPOLY` pour fermer le polygone.

```python
vertices = []
codes = []

# Premier polygone - Rectangle
codes = [Path.MOVETO] + [Path.LINETO]*3 + [Path.CLOSEPOLY]
vertices = [(1, 1), (1, 2), (2, 2), (2, 1), (0, 0)]

# Deuxième polygone - Triangle
codes += [Path.MOVETO] + [Path.LINETO]*2 + [Path.CLOSEPOLY]
vertices += [(4, 4), (5, 5), (5, 4), (0, 0)]
```
