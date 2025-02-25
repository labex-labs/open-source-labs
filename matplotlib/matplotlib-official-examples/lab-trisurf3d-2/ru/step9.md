# Отфильтровываем нежелательные треугольники

Мы отфильтровываем нежелательные треугольники, вычисляя середину каждого треугольника и проверяя, попадает ли она в заданный радиус.

```python
xmid = x[triang.triangles].mean(axis=1)
ymid = y[triang.triangles].mean(axis=1)
mask = xmid**2 + ymid**2 < min_radius**2
triang.set_mask(mask)
```
