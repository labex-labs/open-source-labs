# Создание фигуры и настройка фона

Мы создадим фигуру с использованием метода `plt.figure()`, который создает экземпляр `matplotlib.figure.Figure`. Мы настроим цвет фона фигуры с использованием метода `rect.set_facecolor()`.

```python
fig = plt.figure()
rect = fig.patch  # a rectangle instance
rect.set_facecolor('lightgoldenrodyellow')
```
