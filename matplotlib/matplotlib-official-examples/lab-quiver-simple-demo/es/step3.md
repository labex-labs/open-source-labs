# Crear el gráfico de flechas

Podemos crear el gráfico de flechas usando la función `ax.quiver()`. Pasamos las matrices `X`, `Y`, `U` y `V` como parámetros.

```python
fig, ax = plt.subplots()
q = ax.quiver(X, Y, U, V)
```
