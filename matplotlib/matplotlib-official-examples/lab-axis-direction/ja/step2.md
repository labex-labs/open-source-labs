# 軸を設定する関数を作成する

グラフの軸を設定するための `setup_axes` という関数を作成します。この関数は2つのパラメータを受け取り、`fig` オブジェクトと `pos` オブジェクトです。`fig` オブジェクトはグラフを描画するための figure オブジェクトであり、`pos` オブジェクトは figure 内のサブプロットの位置です。

```python
def setup_axes(fig, pos):
    ax = fig.add_subplot(pos, axes_class=axisartist.Axes)

    ax.set_ylim(-0.1, 1.5)
    ax.set_yticks([0, 1])

    ax.axis[:].set_visible(False)

    ax.axis["x"] = ax.new_floating_axis(1, 0.5)
    ax.axis["x"].set_axisline_style("->", size=1.5)

    return ax
```
