# Création d'une triangulation personnalisée

Dans cette étape, nous allons créer une triangulation personnalisée et masquer les triangles indésirables.

```python
triang = tri.Triangulation(x, y)
triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                         y[triang.triangles].mean(axis=1))
                < min_radius)
```
