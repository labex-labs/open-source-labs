# Crear una trama 3D

A continuación, crearemos una trama 3D utilizando las funciones `plt.figure()` y `fig.add_subplot()`. También usaremos la función `ax.plot_wireframe()` para representar el conjunto de datos como un wireframe.

```python
# Create 3D plot
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# Plot wireframe
ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
```
