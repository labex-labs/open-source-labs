# Criar um Polígono Programaticamente

Para criar um polígono programaticamente, precisamos criar um objeto `Figure` e um objeto `Axes`. Em seguida, podemos criar um objeto `PolygonSelector` e adicionar vértices a ele. Finalmente, podemos plotar o polígono no `Axes`.

```python
fig, ax = plt.subplots()
selector = PolygonSelector(ax, lambda *args: None)

# Add three vertices
selector.verts = [(0.1, 0.4), (0.5, 0.9), (0.3, 0.2)]

# Plot the polygon
ax.add_patch(plt.Polygon(selector.verts, alpha=0.3))
plt.show()
```
