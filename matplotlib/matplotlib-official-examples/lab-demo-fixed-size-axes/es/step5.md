# Agregar ejes a la figura

Agregaremos los ejes a la figura utilizando la función `add_axes()` y pasando la posición del objeto `Divider`.

```python
ax = fig.add_axes(divider.get_position(),
                  axes_locator=divider.new_locator(nx=1, ny=1))
```
