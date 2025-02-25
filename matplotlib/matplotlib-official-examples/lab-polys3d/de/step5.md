# Berechnen der Eckpunkte und der Flächeneigenschaften

Wir berechnen die Eckpunkte und die Flächeneigenschaften mit den Funktionen `vectorize` und `colormaps` aus Matplotlib.

```python
# verts[i] ist eine Liste von (x, y)-Paaren, die Polygon i definieren.
gamma = np.vectorize(math.gamma)
verts = [polygon_under_graph(x, l**x * np.exp(-l) / gamma(x + 1))
         for l in lambdas]
facecolors = plt.colormaps['viridis_r'](np.linspace(0, 1, len(verts)))
```
