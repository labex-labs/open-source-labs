# Densidad variable

En este paso, crearemos un gráfico de flujo con densidad variable. El parámetro `density` controla el número de líneas de corriente que se van a trazar. Valores más altos resultarán en más líneas de corriente.

```python
plt.streamplot(X, Y, U, V, density=[0.5, 1])
plt.title('Varying Density')
plt.show()
```
