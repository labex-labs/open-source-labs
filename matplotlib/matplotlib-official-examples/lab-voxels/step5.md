# Plot the voxel array

Finally, we can use the `Axes3D.voxels` function to plot the voxel array with the specified colors.

```python
ax = plt.figure().add_subplot(projection='3d')
ax.voxels(voxelarray, facecolors=colors, edgecolor='k')

plt.show()
```
