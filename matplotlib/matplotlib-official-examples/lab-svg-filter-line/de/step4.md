# Zeichnen von Schatten

Wir zeichnen Schatten für die Linien, indem wir die gleichen Linien mit einem geringen Offset und grauen Farben verwenden. Wir passen die Farbe und die Z-Reihenfolge der Schattenlinien an, sodass sie unter den ursprünglichen Linien gezeichnet werden. Wir verwenden auch die `offset_copy()`-Methode, um eine Offset-Transformation für die Schattenlinien zu erstellen.

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
