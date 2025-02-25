# Créez le polygone

Nous devons créer le polygone que nous allons éditer en utilisant la classe `Polygon`.

```python
theta = np.arange(0, 2*np.pi, 0.1)
r = 1.5

xs = r * np.cos(theta)
ys = r * np.sin(theta)

poly = Polygon(np.column_stack([xs, ys]), animated=True)
```
