# 軸をフォーマットする

`format_axes`関数を使って、すべてのサブプロットの軸をフォーマットします。この関数は、各サブプロットにテキストラベルを追加し、目盛りラベルを削除します。

```python
def format_axes(fig):
    for i, ax in enumerate(fig.axes):
        ax.text(0.5, 0.5, "ax%d" % (i+1), va="center", ha="center")
        ax.tick_params(labelbottom=False, labelleft=False)

format_axes(fig)
```
