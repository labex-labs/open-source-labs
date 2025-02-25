# Création d'une triangulation de Delaunay

Nous allons créer une triangulation de Delaunay des points. Tout d'abord, nous allons créer les coordonnées x et y des points à l'aide de NumPy.

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

Ensuite, nous allons créer les coordonnées z des points.

```python
z = (np.cos(radii) * np.cos(3 * angles)).flatten()
```

Ensuite, nous allons créer l'objet Triangulation à l'aide de la fonction `Triangulation()` de `matplotlib.tri`. Étant donné que nous ne spécifions pas les triangles, la triangulation de Delaunay sera créée automatiquement.

```python
triang = tri.Triangulation(x, y)
```

Enfin, nous allons masquer les triangles indésirables à l'aide de la fonction `set_mask()`. Dans cet exemple, nous définissons le masque pour exclure les triangles dont le rayon moyen est inférieur à `min_radius`.

```python
triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                         y[triang.triangles].mean(axis=1))
                < min_radius)
```
