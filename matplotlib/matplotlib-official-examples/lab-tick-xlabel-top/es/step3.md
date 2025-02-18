# Mover las etiquetas de las marcas del eje x a la parte superior

Para mover las etiquetas de las marcas del eje x a la parte superior, utilizaremos la función `tick_params()` y estableceremos los parámetros `top` y `labeltop` en `True`, y los parámetros `bottom` y `labelbottom` en `False`.

```python
ax.tick_params(top=True, labeltop=True, bottom=False, labelbottom=False)
```
