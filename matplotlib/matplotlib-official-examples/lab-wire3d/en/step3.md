# Create the Plot

Now that we have our data, we can create the wireframe plot. In this example, we will use the `plot_wireframe()` function to create the plot.

```python
# Create the plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(X, Y, Z, rstride=5, cstride=5)
```
