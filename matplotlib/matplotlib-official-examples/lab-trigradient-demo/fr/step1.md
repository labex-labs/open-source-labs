# Créer les coordonnées x et y des points

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

Explication :

- `n_angles` est le nombre d'angles dans un cercle.
- `n_radii` est le nombre de cercles.
- `min_radius` est le rayon minimum des cercles.
- `radii` est un tableau de rayons.
- `angles` est un tableau d'angles.
- `x` est un tableau de coordonnées x.
- `y` est un tableau de coordonnées y.
