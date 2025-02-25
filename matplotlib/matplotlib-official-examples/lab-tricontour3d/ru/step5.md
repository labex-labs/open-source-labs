# Отфильтровываем нежелательные треугольники

Мы отфильтруем нежелательные треугольники с использованием среднего значения координат x и y.

```python
triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                         y[triang.triangles].mean(axis=1))
                < min_radius)
```
