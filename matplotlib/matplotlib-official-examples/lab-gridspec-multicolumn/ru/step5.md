# Настраиваем подграфики

Мы можем настроить подграфики по необходимости. Например, мы можем установить заголовок фигуры с помощью функции `fig.suptitle()`, а также форматировать оси с помощью функции `format_axes()`.

```python
fig.suptitle("GridSpec")

def format_axes(fig):
    for i, ax in enumerate(fig.axes):
        ax.text(0.5, 0.5, "ax%d" % (i+1), va="center", ha="center")
        ax.tick_params(labelbottom=False, labelleft=False)

format_axes(fig)
```
