# Crear las Líneas Diagonales de Corte

Finalmente, crearemos las líneas diagonales de corte. Crearemos objetos de línea en coordenadas de los ejes y usaremos `ax1.transAxes` y `ax2.transAxes` para transformarlas a las coordenadas de cada subfigura (subplot). Usaremos `ax1.plot` y `ax2.plot` para graficar las líneas. También usaremos `marker` para especificar el estilo del marcador, `markersize` para establecer el tamaño de los marcadores, `linestyle` para establecer el estilo de la línea, `color` para establecer el color de la línea, `mec` para establecer el color del borde del marcador y `mew` para establecer el ancho del borde del marcador.

```python
d =.5
kwargs = dict(marker=[(-1, -d), (1, d)], markersize=12,
              linestyle="none", color='k', mec='k', mew=1, clip_on=False)
ax1.plot([0, 1], [0, 0], transform=ax1.transAxes, **kwargs)
ax2.plot([0, 1], [1, 1], transform=ax2.transAxes, **kwargs)
```
