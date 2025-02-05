# Plot the Surface

Finally, we plot the surface using `plot_trisurf()` function. The triangles in parameter space determine which `x`, `y`, `z` points are connected by an edge.

```python
ax = plt.figure().add_subplot(projection='3d')
ax.plot_trisurf(x, y, z, triangles=tri.triangles, cmap=plt.cm.Spectral)
ax.set_zlim(-1, 1)
```
