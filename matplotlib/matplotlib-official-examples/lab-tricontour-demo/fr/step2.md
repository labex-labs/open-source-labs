# Créer la triangulation

Nous allons créer la triangulation à l'aide de `matplotlib.tri.Triangulation`. Nous n'avons pas besoin de spécifier les triangles, donc la triangulation de Delaunay des points sera créée automatiquement.

```python
triang = tri.Triangulation(x, y)
```
