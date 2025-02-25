# Den 3D-Voxelplot erstellen

Jetzt erstellen wir den 3D-Voxelplot mithilfe der `ax.voxels`-Funktion. Wir übergeben `x`, `y`, `z` und `sphere` als Parameter. Wir fügen auch `facecolors` und `edgecolors` hinzu, indem wir das zuvor definierte `colors`-Array verwenden.

```python
ax = plt.figure().add_subplot(projection='3d')
ax.voxels(x, y, z, sphere,
          facecolors=colors,
          edgecolors=np.clip(2*colors - 0.5, 0, 1),  # heller
          linewidth=0.5)
```
