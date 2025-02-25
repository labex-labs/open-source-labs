# サブプロットをカスタマイズする

必要に応じてサブプロットをカスタマイズできます。たとえば、`fig.suptitle()` 関数を使用してグラフのタイトルを設定し、`format_axes()` 関数を使用して軸をフォーマットできます。

```python
fig.suptitle("GridSpec")

def format_axes(fig):
    for i, ax in enumerate(fig.axes):
        ax.text(0.5, 0.5, "ax%d" % (i+1), va="center", ha="center")
        ax.tick_params(labelbottom=False, labelleft=False)

format_axes(fig)
```
