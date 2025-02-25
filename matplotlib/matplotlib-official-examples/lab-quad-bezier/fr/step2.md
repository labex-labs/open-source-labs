# Création du tracé

Ensuite, nous allons créer l'objet `Path` pour la courbe de Bézier. L'objet `Path` prend une liste de sommets et de codes qui spécifient le type de tracé entre les sommets. Dans ce cas, nous utiliserons un code `MOVETO` pour nous déplacer au point de départ, suivi de deux codes `CURVE3` pour spécifier les points de contrôle et le point d'arrivée, et finalement un code `CLOSEPOLY` pour fermer le tracé.

```python
Path = mpath.Path

bezier_path = Path([(0, 0), (1, 0), (1, 1), (0, 0)],
                   [Path.MOVETO, Path.CURVE3, Path.CURVE3, Path.CLOSEPOLY])
```
