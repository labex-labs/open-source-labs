# Générez des lignes aléatoires

Nous allons générer 12 lignes aléatoires à l'aide de la bibliothèque `numpy` et les tracer à l'aide de la méthode `plot`. Si une ligne intersecte le rectangle, sa couleur sera rouge, sinon bleue. Nous utiliserons la classe `Path` pour créer une ligne et la méthode `intersects_bbox` pour vérifier si elle intersecte le rectangle.

```python
bbox = Bbox.from_bounds(left, bottom, width, height)

for i in range(12):
    vertices = (np.random.random((2, 2)) - 0.5) * 6.0
    path = Path(vertices)
    if path.intersects_bbox(bbox):
        color = 'r'
    else:
        color = 'b'
    ax.plot(vertices[:, 0], vertices[:, 1], color=color)
```
