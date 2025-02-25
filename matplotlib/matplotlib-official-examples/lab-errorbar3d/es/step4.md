# Agregar barras de error al gráfico

Agregamos barras de error a nuestro gráfico utilizando el método `errorbar` del objeto `Axes3D`. Establecemos los parámetros `zuplims` y `zlolims` en arrays que especifican qué puntos de datos tienen límites superiores e inferiores. Establecemos el parámetro `errorevery` para controlar la frecuencia de las barras de error.

```python
estep = 15
i = np.arange(t.size)
zuplims = (i % estep == 0) & (i // estep % 3 == 0)
zlolims = (i % estep == 0) & (i // estep % 3 == 2)

ax.errorbar(x, y, z, 0.2, zuplims=zuplims, zlolims=zlolims, errorevery=estep)
```
