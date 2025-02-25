# Agregar límites a ambos ejes x e y

Finalmente, agregaremos límites a ambos ejes x e y. Usaremos los parámetros `xlolims` y `xuplims` para agregar límites a las barras de error del eje x.

```python
# Grafica una serie con límites inferiores y superiores en x & y
# error constante en x con error variable en y
xerr = 0.2
yerr = np.full_like(x, 0.2)
yerr[[3, 6]] = 0.3

# simula algunos límites modificando los datos anteriores
xlolims = lolims
xuplims = uplims
lolims = np.zeros_like(x)
uplims = np.zeros_like(x)
lolims[[6]] = True  # solo limitado en este índice
uplims[[3]] = True  # solo limitado en este índice

# realiza la gráfica
ax.errorbar(x, y + 2.1, xerr=xerr, yerr=yerr,
            xlolims=xlolims, xuplims=xuplims,
            uplims=uplims, lolims=lolims,
            marker='o', markersize=8, linestyle='none')
```
