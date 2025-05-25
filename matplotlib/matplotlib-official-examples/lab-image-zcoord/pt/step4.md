# Modificar o formatador de coordenadas

Agora, modificaremos o formatador de coordenadas para relatar o valor "z" da imagem do pixel mais próximo, dados x e y. Isso pode ser alcançado personalizando a função `~.axes.Axes.format_coord`.

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
