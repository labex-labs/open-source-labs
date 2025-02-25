# Quitar las etiquetas de las marcas de graduación principales y las marcas de graduación menores

Para simular el comportamiento de centrar las etiquetas entre las marcas de graduación, necesitamos quitar las etiquetas de las marcas de graduación principales y las marcas de graduación menores y solo mostrar las etiquetas de las marcas de graduación menores. Esto se puede hacer utilizando la función `tick_params()` y estableciendo los parámetros `tick1On` y `tick2On` en `False`.

```python
# Quitar las líneas de las marcas de graduación
ax.tick_params(axis='x', which='minor', tick1On=False, tick2On=False)
```
