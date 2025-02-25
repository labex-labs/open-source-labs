# Establecer los límites x utilizando escalares o unidades

En este paso, estableceremos los límites x utilizando escalares o unidades. Utilizaremos el método `set_xlim` para establecer los límites x. Estableceremos los límites x en 2 y 6 utilizando escalares en las unidades actuales para el gráfico de barras en la segunda fila y la primera columna. Estableceremos los límites x en 2 cm y 6 cm utilizando unidades para el gráfico de barras en la segunda fila y la segunda columna.

```python
axs[1, 0].bar(cms, cms, bottom=bottom, width=width, xunits=inch, yunits=cm)
axs[1, 0].set_xlim(2, 6)

axs[1, 1].bar(cms, cms, bottom=bottom, width=width, xunits=inch, yunits=inch)
axs[1, 1].set_xlim(2 * cm, 6 * cm)
```
