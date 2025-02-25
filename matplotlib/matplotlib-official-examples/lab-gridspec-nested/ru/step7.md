# Форматируем оси

Мы будем форматировать оси всех подграфиков с использованием функции `format_axes`. Эта функция добавит текстовую метку к каждому подграфику и удалит метки делений.

```python
def format_axes(fig):
    for i, ax in enumerate(fig.axes):
        ax.text(0.5, 0.5, "ax%d" % (i+1), va="center", ha="center")
        ax.tick_params(labelbottom=False, labelleft=False)

format_axes(fig)
```
