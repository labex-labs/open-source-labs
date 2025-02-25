# Создание круга

Мы создадим круг с использованием функции `make_circle()`. Функция принимает радиус круга в качестве входных данных и возвращает координаты x и y круга.

```python
def make_circle(r):
    t = np.arange(0, np.pi * 2.0, 0.01)
    t = t.reshape((len(t), 1))
    x = r * np.cos(t)
    y = r * np.sin(t)
    return np.hstack((x, y))
```
