# Create Color Maps

We will now create color maps to plot the class decision boundaries. We will use light colors for the background and bold colors for the class colors.

```python
h = 0.05  # step size in the mesh

# Create color maps
cmap_light = ListedColormap(["#FFAAAA", "#AAFFAA", "#AAAAFF"])
cmap_bold = ListedColormap(["#FF0000", "#00FF00", "#0000FF"])
```


