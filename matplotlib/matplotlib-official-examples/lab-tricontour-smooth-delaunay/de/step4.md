# Delaunay-Triangulation durchführen

Wir führen eine Delaunay-Triangulation auf den Testdatenpunkten durch, indem wir die `Triangulation`-Funktion aus dem `matplotlib.tri`-Modul verwenden.

```python
# meshing with Delaunay triangulation
tri = Triangulation(x_test, y_test)
ntri = tri.triangles.shape[0]
```
