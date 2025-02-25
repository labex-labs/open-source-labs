# Realizar una triangulación de Delaunay

Realizamos una triangulación de Delaunay en los puntos de datos de prueba utilizando la función `Triangulation` del módulo `matplotlib.tri`.

```python
# malla con triangulación de Delaunay
tri = Triangulation(x_test, y_test)
ntri = tri.triangles.shape[0]
```
