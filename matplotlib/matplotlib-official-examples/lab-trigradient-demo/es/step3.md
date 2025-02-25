# Crear la Triangulación

```python
triang = Triangulation(x, y)

triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                         y[triang.triangles].mean(axis=1))
                < min_radius)
```

Explicación:

- `Triangulation` es una clase que crea una triangulación de Delaunay a partir de un conjunto de puntos.
- `triang` es una instancia de la clase `Triangulation`.
- `triang.set_mask` desmarca los triángulos no deseados.
