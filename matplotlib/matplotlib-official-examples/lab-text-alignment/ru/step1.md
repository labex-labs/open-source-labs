# Создание прямоугольника

Начнем с создания прямоугольника на графике с использованием функции `Rectangle()` из модуля `matplotlib.patches`. После создания прямоугольника установим его горизонтальные и вертикальные пределы с использованием функций `set_xlim()` и `set_ylim()`. Наконец, добавим прямоугольник на график.

```python
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

fig, ax = plt.subplots()

# Build a rectangle in axes coords
left, width =.25,.5
bottom, height =.25,.5
right = left + width
top = bottom + height
p = Rectangle((left, bottom), width, height, fill=False)
ax.add_patch(p)

# Set the horizontal and vertical limits
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
plt.show()
```
