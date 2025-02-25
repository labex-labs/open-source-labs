# Définir les données

Dans cette étape, vous allez définir les données à tracer. Les données sont un tableau bidimensionnel de valeurs qui représente la surface.

```python
# Delta par défaut est grand car cela le rend rapide et illustre
# l'enregistrement correct entre l'image et les contours.
delta = 0.5

extent = (-3, 4, -4, 3)

x = np.arange(-3.0, 4.001, delta)
y = np.arange(-4.0, 3.001, delta)
X, Y = np.meshgrid(x, y)
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
Z = (Z1 - Z2) * 2
```
