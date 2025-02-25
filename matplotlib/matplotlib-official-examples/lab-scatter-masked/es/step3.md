# Enmascarando puntos de datos y creando el diagrama de dispersión

Enmascaramos los puntos de datos en función de su distancia al origen. Los puntos de datos con una distancia menor que `r0` se enmascaran en `area1`, y aquellos con una distancia mayor o igual a `r0` se enmascaran en `area2`. Luego creamos un diagrama de dispersión de los puntos de datos enmascarados con `marker='^'` y `marker='o'` para `area1` y `area2`, respectivamente.

```python
r = np.sqrt(x ** 2 + y ** 2)
area1 = np.ma.masked_where(r < r0, area)
area2 = np.ma.masked_where(r >= r0, area)
plt.scatter(x, y, s=area1, marker='^', c=c)
plt.scatter(x, y, s=area2, marker='o', c=c)
```
