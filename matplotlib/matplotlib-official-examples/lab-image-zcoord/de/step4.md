# Koordinatenformatter modifizieren

Wir werden nun den Koordinatenformatter so modifizieren, dass der Bild-„z“-Wert des nächsten Pixels bei gegebenen x- und y-Werten ausgegeben wird. Dies kann durch die Anpassung der Funktion `~.axes.Axes.format_coord` erreicht werden.

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
