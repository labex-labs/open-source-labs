# Generar un polígono relleno

Ahora, podemos generar un polígono relleno utilizando la función `fill()`. Usaremos la función de la nieve de Koch para generar las coordenadas del polígono.

```python
x, y = koch_snowflake(order=5)

plt.figure(figsize=(8, 8))
plt.axis('equal')
plt.fill(x, y)
plt.show()
```
