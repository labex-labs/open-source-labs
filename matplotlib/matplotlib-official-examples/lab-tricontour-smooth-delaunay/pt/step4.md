# Realizar a Triangulação de Delaunay

Realizamos uma triangulação de Delaunay nos pontos de dados de teste usando a função `Triangulation` do módulo `matplotlib.tri`.

```python
# meshing with Delaunay triangulation
tri = Triangulation(x_test, y_test)
ntri = tri.triangles.shape[0]
```
