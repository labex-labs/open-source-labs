# Definir una función para obtener el punto de una línea vertical rotada

Definiremos una función que tome las coordenadas del origen, la longitud de la línea y el ángulo en grados como entradas y devuelva las coordenadas xy del extremo de la línea vertical rotado por el ángulo especificado.

```python
def get_point_of_rotated_vertical(origin, line_length, degrees):
    """Return xy coordinates of the vertical line end rotated by degrees."""
    rad = np.deg2rad(-degrees)
    return [origin[0] + line_length * np.sin(rad),
            origin[1] + line_length * np.cos(rad)]
```
