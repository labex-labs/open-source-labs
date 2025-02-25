# Création d'une triangulation

Dans cette étape, nous créons les coordonnées x et y des points à l'aide de `np.linspace` et `np.repeat`. Nous utilisons ensuite la fonction `function_z` définie dans l'étape 1 pour calculer les valeurs de z. Enfin, nous créons la triangulation à l'aide de `tri.Triangulation`.

```python
n_angles = 20
n_radii = 10
min_radius = 0.15
radii = np.linspace(min_radius, 0.95, n_radii)

angles = np.linspace(0, 2 * np.pi, n_angles, endpoint=False)
angles = np.repeat(angles[..., np.newaxis], n_radii, axis=1)
angles[:, 1::2] += np.pi / n_angles

x = (radii * np.cos(angles)).flatten()
y = (radii * np.sin(angles)).flatten()
z = function_z(x, y)

triang = tri.Triangulation(x, y)
triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                         y[triang.triangles].mean(axis=1))
                < min_radius)
```
