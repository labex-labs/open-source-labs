# Establece etiquetas y marcas de z

Establece etiquetas y marcas de z utilizando el método `set`. Estableceremos las etiquetas para las coordenadas X, Y y Z, y estableceremos las marcas de z para mostrar la profundidad de la caja.

```python
# Establece etiquetas y marcas de z
ax.set(
    xlabel='X [km]',
    ylabel='Y [km]',
    zlabel='Z [m]',
    zticks=[0, -150, -300, -450],
)
```
