# Рисуем тени

Мы рисуем тени для линий, используя те же линии с небольшим смещением и серыми цветами. Мы настраиваем цвет и z-порядок тенистых линий, чтобы они были нарисованы ниже исходных линий. Также мы используем метод `offset_copy()`, чтобы создать трансформацию смещения для тенистых линий.

```python
for l in [l1, l2]:
    xx = l.get_xdata()
    yy = l.get_ydata()
    shadow, = ax.plot(xx, yy)
    shadow.update_from(l)

    shadow.set_color("0.2")
    shadow.set_zorder(l.get_zorder() - 0.5)

    transform = mtransforms.offset_copy(l.get_transform(), fig1, x=4.0, y=-6.0, units='points')
    shadow.set_transform(transform)

    shadow.set_gid(l.get_label() + "_shadow")
```
