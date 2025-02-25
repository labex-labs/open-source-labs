# Выполнить Делонева триангуляцию

Мы выполняем Делонева триангуляцию по тестовым точкам данных с использованием функции `Triangulation` из модуля `matplotlib.tri`.

```python
# meshing with Delaunay triangulation
tri = Triangulation(x_test, y_test)
ntri = tri.triangles.shape[0]
```
