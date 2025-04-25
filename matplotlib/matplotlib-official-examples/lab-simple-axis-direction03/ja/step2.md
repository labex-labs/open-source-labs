# 軸の設定関数の作成

軸を設定する関数を作成します。この関数は、x 軸と y 軸の目盛り値を設定します。

```python
def setup_axes(fig, pos):
    ax = fig.add_subplot(pos, axes_class=axisartist.Axes)
    ax.set_yticks([0.2, 0.8])
    ax.set_xticks([0.2, 0.8])
    return ax
```
