# Создайте функцию для анимации

Нам нужно создать функцию `animate`, которая генерирует новые случайные данные и обновляет высоты прямоугольников.

```python
def animate(frame_number):
    # simulate new data coming in
    data = np.random.randn(1000)
    n, _ = np.histogram(data, HIST_BINS)
    for count, rect in zip(n, bar_container.patches):
        rect.set_height(count)
    return bar_container.patches
```
