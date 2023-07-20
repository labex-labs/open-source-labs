# Plot the Surface

```python
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
```

We plot the surface using the `plot_surface()` function. We pass in the `X`, `Y`, and `Z` values as well as the `cmap` parameter set to `cm.coolwarm` to color the surface with the coolwarm colormap. We also set `linewidth=0` to remove the wireframe and `antialiased=False` to make the surface opaque.
