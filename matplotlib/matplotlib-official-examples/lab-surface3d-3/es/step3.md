# Crear colores para la representación gráfica de superficie

En este paso, crearemos los colores para la representación gráfica de superficie. Crearemos una matriz vacía de cadenas con la misma forma que la malla, y la llenaremos con dos colores en un patrón de tablero de ajedrez.

```python
# Create colors for the surface plot
colortuple = ('y', 'b')
colors = np.empty(X.shape, dtype=str)
for y in range(ylen):
    for x in range(xlen):
        colors[y, x] = colortuple[(x + y) % len(colortuple)]
```
