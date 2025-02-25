# Créer un masque

Dans cet exemple, nous créons un masque pour éliminer les triangles indésirables. Nous créons d'abord les espaces de paramètres `rayons` et `angles`.

```python
n_angles = 36
n_radii = 8
min_radius = 0.25
radii = np.linspace(min_radius, 0.95, n_radii)

angles = np.linspace(0, 2*np.pi, n_angles, endpoint=False)
angles = np.repeat(angles[..., np.newaxis], n_radii, axis=1)
angles[:, 1::2] += np.pi/n_angles
```
