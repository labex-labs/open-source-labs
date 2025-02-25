# Создаем Span Selector

Мы создадим объект Span Selector с использованием `matplotlib.widgets.SpanSelector`.

```python
span = SpanSelector(
    ax1,
    onselect,
    "horizontal",
    useblit=True,
    props=dict(alpha=0.5, facecolor="tab:blue"),
    interactive=True,
    drag_from_anywhere=True
)
```
