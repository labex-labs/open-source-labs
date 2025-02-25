# Polygone erstellen

Wir erstellen Polygone mit `Polygon()` und fügen sie zur Liste der Patches hinzu.

```python
for i in range(N):
    polygon = Polygon(np.random.rand(N, 2), closed=True)
    patches.append(polygon)
```
