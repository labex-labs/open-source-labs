# Crear el gráfico de contorno

Ahora crearemos el gráfico de contorno utilizando el método `contourf()`. Este método crea contornos rellenos. Estableceremos el parámetro `cmap` en `cm.coolwarm` para utilizar la paleta de colores frío-cálido.

```python
ax.contourf(X, Y, Z, cmap=cm.coolwarm)
```
