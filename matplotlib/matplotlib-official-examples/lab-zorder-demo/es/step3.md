# Estableciendo zorder para las marcas de graduación y las líneas de cuadrícula

Podemos utilizar el método `set_axisbelow()` o el parámetro `axes.axisbelow` para establecer el `zorder` de las marcas de graduación y las líneas de cuadrícula.

```python
ax = plt.axes()
ax.plot([1, 2, 3], [2, 4, 3])
ax.set_axisbelow(True)
ax.yaxis.grid(color='gray', linestyle='dashed')
```
