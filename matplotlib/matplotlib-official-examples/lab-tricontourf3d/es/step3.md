# Crear una triangulación personalizada

En este paso, crearemos una triangulación personalizada y omitiremos los triángulos no deseados.

```python
triang = tri.Triangulation(x, y)
triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                         y[triang.triangles].mean(axis=1))
                < min_radius)
```
