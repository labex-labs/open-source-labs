# Создайте координаты x и y точек

```python
n_angles = 30
n_radii = 10
min_radius = 0.2
radii = np.linspace(min_radius, 0.95, n_radii)

angles = np.linspace(0, 2 * np.pi, n_angles, endpoint=False)
angles = np.repeat(angles[..., np.newaxis], n_radii, axis=1)
angles[:, 1::2] += np.pi / n_angles

x = (radii*np.cos(angles)).flatten()
y = (radii*np.sin(angles)).flatten()
```

Пояснение:

- `n_angles` - количество углов в круге.
- `n_radii` - количество кругов.
- `min_radius` - минимальный радиус кругов.
- `radii` - массив радиусов.
- `angles` - массив углов.
- `x` - массив координат x.
- `y` - массив координат y.
