# Создайте триангуляцию

```python
triang = Triangulation(x, y)

triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                         y[triang.triangles].mean(axis=1))
                < min_radius)
```

Пояснение:

- `Triangulation` - класс, который создает триангуляцию Делоне из набора точек.
- `triang` - экземпляр класса `Triangulation`.
- `triang.set_mask` скрывает нежелательные треугольники.
