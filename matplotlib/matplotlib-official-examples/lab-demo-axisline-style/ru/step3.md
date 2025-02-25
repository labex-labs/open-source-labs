# Настройка стиля осей

Теперь мы настроим стиль осей, добавив стрелки в концы каждой оси и оси X и Y из начала координат.

```python
for direction in ["xzero", "yzero"]:
    # adds arrows at the ends of each axis
    ax.axis[direction].set_axisline_style("-|>")
    # adds X and Y-axis from the origin
    ax.axis[direction].set_visible(True)

# hides borders
for direction in ["left", "right", "bottom", "top"]:
    ax.axis[direction].set_visible(False)
```
