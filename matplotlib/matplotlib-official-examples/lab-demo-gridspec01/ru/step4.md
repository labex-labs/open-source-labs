# Аннотируем оси

Для аннотации осей мы можем пройтись по осям фигуры и добавить текст с использованием функции `text` и функции `tick_params` для удаления меток делений.

```python
def annotate_axes(fig):
    for i, ax in enumerate(fig.axes):
        ax.text(0.5, 0.5, "ax%d" % (i+1), va="center", ha="center")
        ax.tick_params(labelbottom=False, labelleft=False)
```
