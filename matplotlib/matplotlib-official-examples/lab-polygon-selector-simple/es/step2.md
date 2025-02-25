# Crear un polígono de manera programática

Para crear un polígono de manera programática, necesitamos crear un objeto `Figure` y un objeto `Axes`. Luego, podemos crear un objeto `PolygonSelector` y agregar vértices a él. Finalmente, podemos trazar el polígono en el `Axes`.

```python
fig, ax = plt.subplots()
selector = PolygonSelector(ax, lambda *args: None)

# Agregar tres vértices
selector.verts = [(0.1, 0.4), (0.5, 0.9), (0.3, 0.2)]

# Trazar el polígono
ax.add_patch(plt.Polygon(selector.verts, alpha=0.3))
plt.show()
```
