# Programmgesteuertes Erstellen eines Polygons

Um ein Polygon programmgesteuert zu erstellen, müssen wir ein `Figure`-Objekt und ein `Axes`-Objekt erstellen. Anschließend können wir ein `PolygonSelector`-Objekt erstellen und ihm Eckpunkte hinzufügen. Schließlich können wir das Polygon auf den `Axes` plotten.

```python
fig, ax = plt.subplots()
selector = PolygonSelector(ax, lambda *args: None)

# Fügen Sie drei Eckpunkte hinzu
selector.verts = [(0.1, 0.4), (0.5, 0.9), (0.3, 0.2)]

# Plotten Sie das Polygon
ax.add_patch(plt.Polygon(selector.verts, alpha=0.3))
plt.show()
```
