# Span Selector を作成する

`matplotlib.widgets.SpanSelector` を使用して Span Selector オブジェクトを作成します。

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
