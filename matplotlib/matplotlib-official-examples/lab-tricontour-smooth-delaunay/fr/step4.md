# Effectuer une triangulation de Delaunay

Nous effectuons une triangulation de Delaunay sur les points de données de test à l'aide de la fonction `Triangulation` du module `matplotlib.tri`.

```python
# maillage avec triangulation de Delaunay
tri = Triangulation(x_test, y_test)
ntri = tri.triangles.shape[0]
```
