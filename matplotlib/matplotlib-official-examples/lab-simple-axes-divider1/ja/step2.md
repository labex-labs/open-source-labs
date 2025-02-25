# ヘルパー関数の定義

軸の中央にラベルを配置し、軸の目盛りを削除するためのヘルパー関数 `label_axes()` を定義します。

```python
def label_axes(ax, text):
    """Place a label at the center of an Axes, and remove the axis ticks."""
    ax.text(.5,.5, text, transform=ax.transAxes,
            horizontalalignment="center", verticalalignment="center")
    ax.tick_params(bottom=False, labelbottom=False,
                   left=False, labelleft=False)
```
