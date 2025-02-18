# Traçage du tableau de voxels

Enfin, nous pouvons utiliser la fonction `Axes3D.voxels` pour tracer le tableau de voxels avec les couleurs spécifiées.

```python
ax = plt.figure().add_subplot(projection='3d')
ax.voxels(voxelarray, facecolors=colors, edgecolor='k')

plt.show()
```
