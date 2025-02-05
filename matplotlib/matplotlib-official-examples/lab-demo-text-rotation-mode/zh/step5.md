# 向子图添加文本

我们将使用 `text` 函数向每个子图添加文本。我们将使用参数 `rotation`（旋转）、`horizontalalignment`（水平对齐）、`verticalalignment`（垂直对齐）和 `rotation_mode`（旋转模式）来旋转和对齐文本。我们还将使用 `bbox` 参数来突出显示文本的边界框。

```python
kw = (
    {} if mode == "default" else
    {"bbox": dict(boxstyle="square,pad=0.", ec="none", fc="C1", alpha=0.3)}
)

texts = {}

for i, va in enumerate(va_list):
    for j, ha in enumerate(ha_list):
        ax = axs[i, j]
        tx = ax.text(0.5, 0.5, "Tpg",
                     size="x-large", rotation=40,
                     horizontalalignment=ha, verticalalignment=va,
                     rotation_mode=mode, **kw)
        texts[ax] = tx
```
