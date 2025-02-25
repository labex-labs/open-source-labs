# Erzeuge das Voxel-Diagramm

Schließlich erstellen wir das 3D-Voxel-Diagramm mithilfe der `voxels`-Funktion der `Axes3D`-Klasse in Matplotlib.

```python
ax = plt.figure().add_subplot(projection='3d')
ax.voxels(x, y, z, filled_2, facecolors=fcolors_2, edgecolors=ecolors_2)
ax.set_aspect('equal')

plt.show()
```
