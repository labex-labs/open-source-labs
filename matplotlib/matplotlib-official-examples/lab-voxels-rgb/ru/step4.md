# Объединение цветов

Теперь мы объединим компоненты RGB-цвета в одномерный массив формы `(17, 17, 17, 3)`.

```python
colors = np.zeros(sphere.shape + (3,))
colors[..., 0] = rc
colors[..., 1] = gc
colors[..., 2] = bc
```
