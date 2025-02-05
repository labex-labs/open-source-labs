# Create the voxel plot

Finally, we create the 3D voxel plot using the `voxels` function of the `Axes3D` class in Matplotlib.

```python
ax = plt.figure().add_subplot(projection='3d')
ax.voxels(x, y, z, filled_2, facecolors=fcolors_2, edgecolors=ecolors_2)
ax.set_aspect('equal')

plt.show()
```
