# Crear la representación de voxeles

Finalmente, creamos la representación de voxeles 3D utilizando la función `voxels` de la clase `Axes3D` en Matplotlib.

```python
ax = plt.figure().add_subplot(projection='3d')
ax.voxels(x, y, z, filled_2, facecolors=fcolors_2, edgecolors=ecolors_2)
ax.set_aspect('equal')

plt.show()
```
