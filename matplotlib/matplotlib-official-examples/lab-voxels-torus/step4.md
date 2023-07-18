# Create the 3D Voxel Plot

Now we create the 3D voxel plot using the `ax.voxels` function. We pass in `x`, `y`, `z`, and `sphere` as the parameters. We also add `facecolors` and `edgecolors` using the `colors` array we defined earlier.

```python
ax = plt.figure().add_subplot(projection='3d')
ax.voxels(x, y, z, sphere,
          facecolors=colors,
          edgecolors=np.clip(2*colors - 0.5, 0, 1),  # brighter
          linewidth=0.5)
```
