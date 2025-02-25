# Koordinaten erstellen

Als nächstes werden wir die x-, y- und z-Koordinaten der Punkte erstellen. Wir werden das Gitter in Polarkoordinaten erstellen und x, y, z berechnen.

```python
n_angles = 48
n_radii = 8
min_radius = 0.25

radii = np.linspace(min_radius, 0.95, n_radii)
angles = np.linspace(0, 2*np.pi, n_angles, endpoint=False)
angles = np.repeat(angles[..., np.newaxis], n_radii, axis=1)
angles[:, 1::2] += np.pi/n_angles

x = (radii*np.cos(angles)).flatten()
y = (radii*np.sin(angles)).flatten()
z = (np.cos(radii)*np.cos(3*angles)).flatten()
```
