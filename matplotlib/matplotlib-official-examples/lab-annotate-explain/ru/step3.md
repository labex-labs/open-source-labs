# Добавить эллипс на график

В этом шаге мы добавим эллипс на график. Мы будем использовать функцию `Ellipse` для создания эллипса и настроим свойства эллипса, такие как позиция, ширина, высота и угол.

```python
ax = axs.flat[1]
ax.plot([x1, x2], [y1, y2], ".")
el = mpatches.Ellipse((x1, y1), 0.3, 0.4, angle=30, alpha=0.2)
ax.add_artist(el)
```
