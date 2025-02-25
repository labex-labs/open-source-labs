# Créez des polygones

Nous créons des polygones à l'aide de `Polygon()` et les ajoutons à la liste de patches.

```python
for i in range(N):
    polygon = Polygon(np.random.rand(N, 2), closed=True)
    patches.append(polygon)
```
