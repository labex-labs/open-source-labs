# サブプロットにテキストを追加する

`text` 関数を使って各サブプロットにテキストを追加します。`rotation`、`horizontalalignment`、`verticalalignment`、`rotation_mode` の各パラメータを使ってテキストを回転させて配置します。また、`bbox` パラメータを使ってテキストの境界ボックスを強調します。

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
