# Establecer la fuente para el título

Establecemos la fuente para el título de la gráfica utilizando el método `set_title()` de la clase `Axes`. Pasamos la ruta de la fuente como parámetro `font` y el nombre del archivo de fuente como título de la gráfica.

```python
ax.set_title(f'This is a special font: {fpath.name}', font=fpath)
```
