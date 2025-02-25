# Definir la función de actualización

Definimos una función que actualiza el gráfico para cada fotograma de la animación. La función toma tres entradas: `num` es el número actual del fotograma, `walks` es una lista de todos los paseos aleatorios y `lines` es una lista de todas las líneas en el gráfico. Para cada línea y paseo, actualizamos los datos de las coordenadas x, y y z de la línea hasta el número actual de fotograma. Utilizamos `line.set_data()` y `line.set_3d_properties()` para actualizar las coordenadas x-y y z, respectivamente.

```python
def update_lines(num, walks, lines):
    for line, walk in zip(lines, walks):
        # NOTE: there is no.set_data() for 3 dim data...
        line.set_data(walk[:num, :2].T)
        line.set_3d_properties(walk[:num, 2])
    return lines
```
