# Compute the Vertices and Facecolors

We compute the vertices and facecolors using the `vectorize` and `colormaps` functions from Matplotlib.

```python
# verts[i] is a list of (x, y) pairs defining polygon i.
gamma = np.vectorize(math.gamma)
verts = [polygon_under_graph(x, l**x * np.exp(-l) / gamma(x + 1))
         for l in lambdas]
facecolors = plt.colormaps['viridis_r'](np.linspace(0, 1, len(verts)))
```
