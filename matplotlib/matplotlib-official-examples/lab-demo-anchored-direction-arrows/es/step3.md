# Crear una flecha simple

Ahora, crearemos una flecha de dirección anclada simple utilizando la clase `AnchoredDirectionArrows`. Esta flecha indicará las direcciones X e Y en la gráfica.

```python
# Simple example
simple_arrow = AnchoredDirectionArrows(ax.transAxes, 'X', 'Y')
ax.add_artist(simple_arrow)
```
