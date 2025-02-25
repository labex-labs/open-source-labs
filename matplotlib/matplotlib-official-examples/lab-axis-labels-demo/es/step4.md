# Establecer la posición de la etiqueta de la barra de colores

Podemos establecer la posición de la etiqueta de la barra de colores utilizando el método `colorbar` y el método `set_label`. Podemos establecer la posición en `'superior'`, `'inferior'`, `'izquierda'` o `'derecha'`. En este ejemplo, estableceremos la posición en `'superior'`.

```python
cbar = fig.colorbar(sc)
cbar.set_label("EtiquetaZ", loc='top')
```
