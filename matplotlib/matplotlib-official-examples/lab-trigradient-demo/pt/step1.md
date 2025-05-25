# Criar as coordenadas x e y dos pontos

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

Explicação:

- `n_angles` é o número de ângulos em um círculo.
- `n_radii` é o número de círculos.
- `min_radius` é o raio mínimo dos círculos.
- `radii` é um array de raios.
- `angles` é um array de ângulos.
- `x` é um array de coordenadas x.
- `y` é um array de coordenadas y.
