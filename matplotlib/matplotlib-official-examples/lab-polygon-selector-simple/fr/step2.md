# Créer un polygone de manière programmée

Pour créer un polygone de manière programmée, nous devons créer un objet `Figure` et un objet `Axes`. Ensuite, nous pouvons créer un objet `PolygonSelector` et y ajouter des sommets. Enfin, nous pouvons tracer le polygone sur l'`Axes`.

```python
fig, ax = plt.subplots()
selector = PolygonSelector(ax, lambda *args: None)

# Ajoutez trois sommets
selector.verts = [(0.1, 0.4), (0.5, 0.9), (0.3, 0.2)]

# Tracez le polygone
ax.add_patch(plt.Polygon(selector.verts, alpha=0.3))
plt.show()
```
