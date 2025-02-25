# 軸に注釈を付ける

軸に注釈を付けるには、グラフの軸をループして、`text`関数を使ってテキストを追加し、目盛りのラベルを削除するために`tick_params`関数を使います。

```python
def annotate_axes(fig):
    for i, ax in enumerate(fig.axes):
        ax.text(0.5, 0.5, "ax%d" % (i+1), va="center", ha="center")
        ax.tick_params(labelbottom=False, labelleft=False)
```
