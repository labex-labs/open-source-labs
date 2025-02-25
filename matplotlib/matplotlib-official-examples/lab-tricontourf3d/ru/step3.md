# Создание пользовательской триангуляции

В этом шаге мы создадим пользовательскую триангуляцию и исключим нежелательные треугольники.

```python
triang = tri.Triangulation(x, y)
triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                         y[triang.triangles].mean(axis=1))
                < min_radius)
```
