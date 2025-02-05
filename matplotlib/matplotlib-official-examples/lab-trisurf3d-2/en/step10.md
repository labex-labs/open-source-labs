# Plot the Surface

Finally, we plot the surface using `plot_trisurf()` function.

```python
ax = plt.figure().add_subplot(projection='3d')
ax.plot_trisurf(triang, z, cmap=plt.cm.CMRmap)
```
