# Modificar el formateador de coordenadas

Ahora modificaremos el formateador de coordenadas para reportar el valor "z" de la imagen del píxel más cercano dado x e y. Esto se puede lograr personalizando la función `~.axes.Axes.format_coord`.

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
