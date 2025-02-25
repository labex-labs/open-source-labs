# Agregar líneas verticales al histograma

Para facilitar la visualización del efecto del umbralado, agregaremos líneas verticales al histograma para indicar los valores actuales del umbral. Crearemos dos líneas para los valores inferior y superior del umbral, respectivamente.

```python
lower_limit_line = axs[1].axvline(slider.val[0], color='k')
upper_limit_line = axs[1].axvline(slider.val[1], color='k')
```
