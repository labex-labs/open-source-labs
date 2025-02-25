# Définition des coordonnées et des couleurs

Ensuite, nous devons définir les coordonnées et les couleurs pour le graphique. Dans cet exemple, nous allons utiliser la fonction `np.indices` pour créer une grille de valeurs 17x17x17 pour les couleurs RGB.

```python
r, g, b = np.indices((17, 17, 17)) / 16.0
```

Nous définirons également une fonction `midpoints` pour trouver les points moyens entre les valeurs de la grille. Cela sera utilisé plus tard pour créer la sphère.

```python
def midpoints(x):
    sl = ()
    for _ in range(x.ndim):
        x = (x[sl + np.index_exp[:-1]] + x[sl + np.index_exp[1:]]) / 2.0
        sl += np.index_exp[:]
    return x
```
