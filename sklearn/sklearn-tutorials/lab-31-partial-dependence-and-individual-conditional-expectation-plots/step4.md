# Create and visualize partial dependence plots

```python
fig, ax = plot_partial_dependence(model, X, features=[(0, 1), (2, 3)], feature_names=feature_names, grid_resolution=20)

# Set figure size and title
fig.set_size_inches(10, 8)
fig.suptitle('Partial Dependence Plots')

plt.show()
```
