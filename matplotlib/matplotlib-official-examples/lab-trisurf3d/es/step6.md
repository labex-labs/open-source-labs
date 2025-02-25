# Crear la superficie 3D

Crearemos la superficie 3D utilizando la función `plot_trisurf`:

```python
ax = plt.figure().add_subplot(projection='3d')
ax.plot_trisurf(x, y, z, linewidth=0.2, antialiased=True)

plt.show()
```
