# 軸の内側にラベルを付ける

サブプロットにラベルを付ける最も簡単な方法は、軸の内側にラベルを置くことです。これは、`ax.text` メソッドを使用することで達成できます。各サブプロットをループし、`ax.transAxes` を使って軸の内側にラベルを追加します。

```python
for label, ax in axs.items():
    # label physical distance in and down:
    trans = mtransforms.ScaledTranslation(10/72, -5/72, fig.dpi_scale_trans)
    ax.text(0.0, 1.0, label, transform=ax.transAxes + trans,
            fontsize='medium', verticalalignment='top', fontfamily='serif',
            bbox=dict(facecolor='0.7', edgecolor='none', pad=3.0))
```
