# Plotting the Voxel Plot

Finally, we can plot the voxel plot using the `ax.voxels` function. We will pass in the RGB values, the condition for the sphere, the face colors, edge colors, and linewidth.

```python
ax = plt.figure().add_subplot(projection='3d')
ax.voxels(r, g, b, sphere,
          facecolors=colors,
          edgecolors=np.clip(2*colors - 0.5, 0, 1),  # brighter
          linewidth=0.5)
ax.set(xlabel='r', ylabel='g', zlabel='b')
ax.set_aspect('equal')
plt.show()
```
