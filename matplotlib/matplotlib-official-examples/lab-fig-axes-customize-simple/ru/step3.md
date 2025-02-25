# Добавление осей на фигуру

Мы добавим оси на фигуру с использованием метода `fig.add_axes()`. Также настроим цвет фона осей с использованием метода `rect.set_facecolor()`.

```python
ax1 = fig.add_axes([0.1, 0.3, 0.4, 0.4])
rect = ax1.patch
rect.set_facecolor('lightslategray')
```
