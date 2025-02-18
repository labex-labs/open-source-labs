# Plotten des Voxel-Arrays

Schließlich können wir die Funktion `Axes3D.voxels` verwenden, um das Voxel-Array mit den angegebenen Farben zu plotten.

```python
ax = plt.figure().add_subplot(projection='3d')
ax.voxels(voxelarray, facecolors=colors, edgecolor='k')

plt.show()
```
