# Erstellen eines Span Selectors

Wir werden ein Span Selector-Objekt mit `matplotlib.widgets.SpanSelector` erstellen.

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
