# Erstellen einer Delaunay-Triangulation

Wir werden eine Delaunay-Triangulation der Punkte erstellen. Zunächst werden wir die x- und y-Koordinaten der Punkte mit NumPy erstellen.

```python
n_angles = 36
n_radii = 8
min_radius = 0.25
radii = np.linspace(min_radius, 0.95, n_radii)
angles = np.linspace(0, 2 * np.pi, n_angles, endpoint=False)
angles = np.repeat(angles[..., np.newaxis], n_radii, axis=1)
angles[:, 1::2] += np.pi / n_angles
x = (radii * np.cos(angles)).flatten()
y = (radii * np.sin(angles)).flatten()
```

Dann werden wir die z-Koordinaten der Punkte erstellen.

```python
z = (np.cos(radii) * np.cos(3 * angles)).flatten()
```

Als nächstes werden wir das Triangulationsobjekt mit der `Triangulation()`-Funktion aus `matplotlib.tri` erstellen. Da wir die Dreiecke nicht angeben, wird automatisch die Delaunay-Triangulation erstellt.

```python
triang = tri.Triangulation(x, y)
```

Schließlich werden wir die unerwünschten Dreiecke mit der `set_mask()`-Funktion ausblenden. In diesem Beispiel setzen wir die Maske, um Dreiecke mit einem mittleren Radius kleiner als `min_radius` auszuschließen.

```python
triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                         y[triang.triangles].mean(axis=1))
                < min_radius)
```
