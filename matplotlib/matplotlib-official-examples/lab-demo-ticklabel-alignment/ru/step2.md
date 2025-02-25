# Определяем функцию для настройки осей

Для упрощения кода можно определить функцию, которая принимает объект фигуры и позицию в качестве входных данных и возвращает объект оси с пользовательскими метками делений.

```python
def setup_axes(fig, pos):
    ax = fig.add_subplot(pos, axes_class=axisartist.Axes)
    ax.set_yticks([0.2, 0.8], labels=["short", "loooong"])
    ax.set_xticks([0.2, 0.8], labels=[r"$\frac{1}{2}\pi$", r"$\pi$"])
    return ax
```
