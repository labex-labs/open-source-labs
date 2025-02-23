# Создаем график

Создадим простой график параболы с использованием функции `linspace` из NumPy для генерации 1000 значений для x в диапазоне от -5 до 5, а затем вычислим y как квадрат x.

```python
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_title("Cursor Tracking x Position")

x = np.linspace(-5, 5, 1000)
y = x**2

line, = ax.plot(x, y)
ax.set_xlim(-5, 5)
ax.set_ylim(0, 25)
```
