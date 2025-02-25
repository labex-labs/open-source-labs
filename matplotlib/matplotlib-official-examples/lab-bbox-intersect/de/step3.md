# Generieren von zufälligen Linien

Wir werden 12 zufällige Linien mit der `numpy`-Bibliothek generieren und sie mit der `plot`-Methode darstellen. Wenn eine Linie das Rechteck schneidet, wird ihre Farbe rot sein, andernfalls blau. Wir werden die `Path`-Klasse verwenden, um eine Linie zu erstellen und die `intersects_bbox`-Methode, um zu überprüfen, ob sie das Rechteck schneidet.

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
