# Маскирование нежелательных треугольников

Мы удалим нежелательные треугольники, вычислив среднее значение координат x и y вершин каждого треугольника и сравнив его с минимальным радиусом.

```python
triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                         y[triang.triangles].mean(axis=1))
                < min_radius)
```
