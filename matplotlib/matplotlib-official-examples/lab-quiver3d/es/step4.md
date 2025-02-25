# Crear el gráfico de flechas

Con la cuadrícula y la dirección de las flechas definidas, podemos crear el gráfico de flechas. En este ejemplo, usaremos la función `quiver` de Matplotlib para crear el gráfico. El parámetro `length` establece la longitud de las flechas y el parámetro `normalize` normaliza las flechas a una longitud de 1.

```python
ax.quiver(x, y, z, u, v, w, length=0.1, normalize=True)
```
