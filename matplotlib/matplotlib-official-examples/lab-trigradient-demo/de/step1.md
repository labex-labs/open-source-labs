# Erstelle die x- und y-Koordinaten der Punkte

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

Erklärung:

- `n_angles` ist die Anzahl der Winkel in einem Kreis.
- `n_radii` ist die Anzahl der Kreise.
- `min_radius` ist der minimale Radius der Kreise.
- `radii` ist ein Array von Radien.
- `angles` ist ein Array von Winkeln.
- `x` ist ein Array von x-Koordinaten.
- `y` ist ein Array von y-Koordinaten.
