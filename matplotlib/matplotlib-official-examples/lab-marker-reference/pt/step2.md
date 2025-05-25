# Marcadores Preenchidos (Filled Markers)

Marcadores preenchidos são o oposto de marcadores não preenchidos. O código a seguir demonstra como criar marcadores preenchidos:

```python
fig, axs = plt.subplots(ncols=2)
fig.suptitle('Filled markers', fontsize=14)
for ax, markers in zip(axs, split_list(Line2D.filled_markers)):
    for y, marker in enumerate(markers):
        ax.text(-0.5, y, repr(marker), **text_style)
        ax.plot([y] * 3, marker=marker, **marker_style)
    format_axes(ax)
```
