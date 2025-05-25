# Calcular os Vértices e as Cores das Faces

Calculamos os vértices e as cores das faces usando as funções `vectorize` e `colormaps` do Matplotlib.

```python
# verts[i] is a list of (x, y) pairs defining polygon i.
gamma = np.vectorize(math.gamma)
verts = [polygon_under_graph(x, l**x * np.exp(-l) / gamma(x + 1))
         for l in lambdas]
facecolors = plt.colormaps['viridis_r'](np.linspace(0, 1, len(verts)))
```
