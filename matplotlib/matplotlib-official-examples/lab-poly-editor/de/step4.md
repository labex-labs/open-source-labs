# Erstellen des Polygons

Wir müssen das Polygon erstellen, das wir mit der `Polygon`-Klasse bearbeiten werden.

```python
theta = np.arange(0, 2*np.pi, 0.1)
r = 1.5

xs = r * np.cos(theta)
ys = r * np.sin(theta)

poly = Polygon(np.column_stack([xs, ys]), animated=True)
```
