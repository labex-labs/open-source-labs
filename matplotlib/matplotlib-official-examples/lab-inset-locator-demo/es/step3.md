# Desactivar las etiquetas de las marcas de graduación

Para eliminar las etiquetas de las marcas de graduación de cada uno de los insets, podemos usar el método `tick_params()` y establecer `labelleft` y `labelbottom` en `False`.

```python
# Desactiva las etiquetas de las marcas de graduación de los insets
for axi in [axins, axins2, axins3, axins4]:
    axi.tick_params(labelleft=False, labelbottom=False)
```
