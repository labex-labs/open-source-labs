# Calculez les sommets et les couleurs de face

Nous calculons les sommets et les couleurs de face en utilisant les fonctions `vectorize` et `colormaps` de Matplotlib.

```python
# verts[i] est une liste de paires (x, y) définissant le polygone i.
gamma = np.vectorize(math.gamma)
verts = [polygon_under_graph(x, l**x * np.exp(-l) / gamma(x + 1))
         for l in lambdas]
facecolors = plt.colormaps['viridis_r'](np.linspace(0, 1, len(verts)))
```
