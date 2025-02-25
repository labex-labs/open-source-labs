# Настройка интерактивности

Нам нужно настроить интерактивность для обновления треугольника под указателем мыши. Мы будем использовать событие `motion_notify_event`, чтобы определить, когда указатель мыши перемещается по графику. Мы создадим функцию `on_mouse_move()`, которая будет получать треугольник под указателем мыши с использованием объекта TriFinder, обновлять многоугольник вершинами треугольника и обновлять заголовок графика индексом треугольника.

```python
def on_mouse_move(event):
    if event.inaxes is None:
        tri = -1
    else:
        tri = trifinder(event.xdata, event.ydata)
    update_polygon(tri)
    ax.set_title(f'Triangle {tri}')
    event.canvas.draw()

fig.canvas.mpl_connect('motion_notify_event', on_mouse_move)
```
