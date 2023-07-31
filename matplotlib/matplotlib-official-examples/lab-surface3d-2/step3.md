# Creating the 3D Surface Plot

Now we can create the 3D surface plot. We start by creating a figure and adding a subplot with the `projection='3d'` argument. Then, we use the `plot_surface()` function to plot the surface using the data we created in the previous step.

```python
# Plot the surface
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(x, y, z)
```
