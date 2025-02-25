# Crear el gráfico

Ahora, crearemos el gráfico utilizando la función `tricontourf()` y personalizaremos el ángulo de vista.

```python
ax = plt.figure().add_subplot(projection='3d')
ax.tricontourf(triang, z, cmap=plt.cm.CMRmap)
ax.view_init(elev=45.)

plt.show()
```
