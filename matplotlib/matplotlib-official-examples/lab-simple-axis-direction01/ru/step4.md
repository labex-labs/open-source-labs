# Задаем метки осей

Мы задаем метки осей для левой и правой сторон графика с использованием функции `ax1.axis[]`. Мы также задаем направление меток делений с использованием функции `set_axis_direction()`.

```python
ax1.axis["left"].major_ticklabels.set_axis_direction("top")
ax1.axis["left"].label.set_text("Left label")

ax1.axis["right"].label.set_visible(True)
ax1.axis["right"].label.set_text("Right label")
ax1.axis["right"].label.set_axis_direction("left")
```
