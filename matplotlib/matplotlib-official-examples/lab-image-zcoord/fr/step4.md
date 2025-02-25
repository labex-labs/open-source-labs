# Modifier le formatteur de coordonnées

Nous allons maintenant modifier le formatteur de coordonnées pour afficher la valeur "z" de l'image du pixel le plus proche en fonction des coordonnées x et y. Cela peut être réalisé en personnalisant la fonction `~.axes.Axes.format_coord`.

```python
def format_coord(x, y):
    col = round(x)
    row = round(y)
    nrows, ncols = X.shape
    if 0 <= col < ncols and 0 <= row < nrows:
        z = X[row, col]
        return f'x={x:1.4f}, y={y:1.4f}, z={z:1.4f}'
    else:
        return f'x={x:1.4f}, y={y:1.4f}'

ax.format_coord = format_coord
```
