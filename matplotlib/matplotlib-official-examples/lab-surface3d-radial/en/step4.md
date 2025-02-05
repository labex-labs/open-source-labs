# Plot the Surface

In this step, we will plot the surface using Matplotlib's `plot_surface()` function. We will use the colormap `YlGnBu_r` to set the color of the surface.

```python
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(X, Y, Z, cmap=plt.cm.YlGnBu_r)
```
