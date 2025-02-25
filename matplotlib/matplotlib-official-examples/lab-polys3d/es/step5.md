# Calcular los vértices y los colores de las caras

Calculamos los vértices y los colores de las caras utilizando las funciones `vectorize` y `colormaps` de Matplotlib.

```python
# verts[i] es una lista de pares (x, y) que definen el polígono i.
gamma = np.vectorize(math.gamma)
verts = [polygon_under_graph(x, l**x * np.exp(-l) / gamma(x + 1))
         for l in lambdas]
facecolors = plt.colormaps['viridis_r'](np.linspace(0, 1, len(verts)))
```
