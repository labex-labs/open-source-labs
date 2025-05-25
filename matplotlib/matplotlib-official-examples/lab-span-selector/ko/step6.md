# Span Selector 생성

`matplotlib.widgets.SpanSelector`를 사용하여 Span Selector 객체를 생성합니다.

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
