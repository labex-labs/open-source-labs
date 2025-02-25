# Crear un gráfico tridimensional

Creamos un gráfico tridimensional utilizando `matplotlib`. Agregamos una línea vacía para cada paseo aleatorio al gráfico. Establecemos los límites para los ejes x, y y z entre 0 y 1.

```python
# Attaching 3D axis to the figure
fig = plt.figure()
ax = fig.add_subplot(projection="3d")

# Create lines initially without data
lines = [ax.plot([], [], [])[0] for _ in walks]

# Setting the axes properties
ax.set(xlim3d=(0, 1), xlabel='X')
ax.set(ylim3d=(0, 1), ylabel='Y')
ax.set(zlim3d=(0, 1), zlabel='Z')
```
