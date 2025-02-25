# Создаем класс UpdatingRect

Мы создадим подкласс Rectangle под названием UpdatingRect. Этот класс вызывается с экземпляром Axes, заставляя прямоугольник обновить свою форму, чтобы соответствовать границам Axes.

```python
class UpdatingRect(Rectangle):
    def __call__(self, ax):
        self.set_bounds(*ax.viewLim.bounds)
        ax.figure.canvas.draw_idle()
```
