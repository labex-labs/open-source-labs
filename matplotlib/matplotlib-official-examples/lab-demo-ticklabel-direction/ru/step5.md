# Настраиваемое направление подписей делений

В этом шаге мы создадим вложенный график с настраиваемым направлением подписей делений.

```python
ax = setup_axes(fig, 132)
ax.axis["left"].set_axis_direction("right")
ax.axis["bottom"].set_axis_direction("top")
ax.axis["right"].set_axis_direction("left")
ax.axis["top"].set_axis_direction("bottom")
```
