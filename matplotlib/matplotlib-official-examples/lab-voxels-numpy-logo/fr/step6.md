# Créer le tracé en voxels

Enfin, nous créons le tracé en voxels 3D à l'aide de la fonction `voxels` de la classe `Axes3D` dans Matplotlib.

```python
ax = plt.figure().add_subplot(projection='3d')
ax.voxels(x, y, z, filled_2, facecolors=fcolors_2, edgecolors=ecolors_2)
ax.set_aspect('equal')

plt.show()
```
