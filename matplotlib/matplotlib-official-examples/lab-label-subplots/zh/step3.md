# 在坐标轴内添加标签

给子图添加标签最简单的方法是将标签放在坐标轴内。我们可以通过使用 `ax.text` 方法来实现这一点。我们将遍历每个子图，并使用 `ax.transAxes` 在坐标轴内添加标签。

```python
for label, ax in axs.items():
    # label physical distance in and down:
    trans = mtransforms.ScaledTranslation(10/72, -5/72, fig.dpi_scale_trans)
    ax.text(0.0, 1.0, label, transform=ax.transAxes + trans,
            fontsize='medium', verticalalignment='top', fontfamily='serif',
            bbox=dict(facecolor='0.7', edgecolor='none', pad=3.0))
```
