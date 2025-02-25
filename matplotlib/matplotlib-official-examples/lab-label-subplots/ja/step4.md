# 軸の外側にラベルを付ける

我々は、軸の外側にラベルを付けたい場合がありますが、それでも互いに整列させたいと思うかもしれません。この場合、少し異なる変換を使用します。

```python
for label, ax in axs.items():
    # label physical distance to the left and up:
    trans = mtransforms.ScaledTranslation(-20/72, 7/72, fig.dpi_scale_trans)
    ax.text(0.0, 1.0, label, transform=ax.transAxes + trans,
            fontsize='medium', va='bottom', fontfamily='serif')
```
