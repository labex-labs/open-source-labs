# Создаем функцию hatches_plot

Функция hatches_plot создаст прямоугольник с указанным штриховочным паттерном и добавит его на ось. Также она добавит текст с штриховочным паттерном.

```python
def hatches_plot(ax, h):
    ax.add_patch(Rectangle((0, 0), 2, 2, fill=False, hatch=h))
    ax.text(1, -0.5, f"' {h} '", size=15, ha="center")
    ax.axis('equal')
    ax.axis('off')
```
