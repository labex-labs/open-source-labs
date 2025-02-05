# 在坐标轴外添加标签

我们可能希望标签在坐标轴外，但仍相互对齐。在这种情况下，我们使用稍有不同的变换。

```python
for label, ax in axs.items():
    # label physical distance to the left and up:
    trans = mtransforms.ScaledTranslation(-20/72, 7/72, fig.dpi_scale_trans)
    ax.text(0.0, 1.0, label, transform=ax.transAxes + trans,
            fontsize='medium', va='bottom', fontfamily='serif')
```
