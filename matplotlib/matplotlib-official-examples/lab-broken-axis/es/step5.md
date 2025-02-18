# Establecer los Límites del Eje Y

Limitaremos el eje y de la primera subfigura (subplot) para mostrar solo los valores atípicos (outliers) y el de la segunda subfigura para mostrar la mayoría de los datos. Usaremos `ax1.set_ylim` y `ax2.set_ylim` para establecer los límites del eje y.

```python
ax1.set_ylim(.78, 1.)  # solo valores atípicos
ax2.set_ylim(0,.22)  # la mayoría de los datos
```
