# Créer la triangulation

```python
triang = Triangulation(x, y)

triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                         y[triang.triangles].mean(axis=1))
                < min_radius)
```

Explication :

- `Triangulation` est une classe qui crée une triangulation de Delaunay à partir d'un ensemble de points.
- `triang` est une instance de la classe `Triangulation`.
- `triang.set_mask` masque les triangles indésirables.
