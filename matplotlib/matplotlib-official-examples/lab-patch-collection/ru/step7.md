# Создаем полигоны

Мы создаем полигоны с использованием `Polygon()` и добавляем их в список патчей.

```python
for i in range(N):
    polygon = Polygon(np.random.rand(N, 2), closed=True)
    patches.append(polygon)
```
