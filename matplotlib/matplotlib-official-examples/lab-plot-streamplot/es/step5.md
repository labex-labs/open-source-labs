# Ancho de línea variable

En este paso, crearemos un gráfico de flujo con ancho de línea variable. El parámetro `linewidth` controla el ancho de las líneas de corriente. Aquí, estamos usando la matriz `speed` que calculamos anteriormente para variar el ancho de línea.

```python
lw = 5*speed / speed.max()
plt.streamplot(X, Y, U, V, density=0.6, color='k', linewidth=lw)
plt.title('Varying Line Width')
plt.show()
```
