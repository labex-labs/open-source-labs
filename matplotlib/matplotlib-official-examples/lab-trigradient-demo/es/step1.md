# Crear las coordenadas x e y de los puntos

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

Explicación:

- `n_angles` es el número de ángulos en un círculo.
- `n_radii` es el número de círculos.
- `min_radius` es el radio mínimo de los círculos.
- `radii` es una matriz de radios.
- `angles` es una matriz de ángulos.
- `x` es una matriz de coordenadas x.
- `y` es una matriz de coordenadas y.
