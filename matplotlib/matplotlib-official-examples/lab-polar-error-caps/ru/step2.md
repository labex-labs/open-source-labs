# Создаем данные

В этом шаге мы создадим данные для нашего графика с погрешностными полосами. Мы будем использовать NumPy для создания массива значений theta и массива соответствующих значений радиуса.

```python
theta = np.arange(0, 2 * np.pi, np.pi / 4)
r = theta / np.pi / 2 + 0.5
```
