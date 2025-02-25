# Отфильтруйте нежелательные треугольники

Мы будем использовать метод `set_mask`, чтобы скрыть нежелательные треугольники.

```python
triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                         y[triang.triangles].mean(axis=1))
                < min_radius)
```
