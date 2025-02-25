# Crear un eje insertado

Crea un eje insertado utilizando la función `zoomed_inset_axes`. Establece el nivel de zoom y la ubicación del eje insertado dentro de la gráfica principal.

```python
axins = zoomed_inset_axes(ax, zoom=2, loc='upper left')
axins.set(xticks=[], yticks=[])
```
