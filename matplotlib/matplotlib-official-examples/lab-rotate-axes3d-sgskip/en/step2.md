# Create a 3D Plot

Next, we will create a 3D plot using the `plt.figure()` and `fig.add_subplot()` functions. We will also use the `ax.plot_wireframe()` function to plot the dataset as a wireframe.

```python
# Create 3D plot
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# Plot wireframe
ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
```
