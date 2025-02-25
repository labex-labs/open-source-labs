# Marcadores con relleno

Los marcadores con relleno son lo contrario de los marcadores sin relleno. El siguiente código demuestra cómo crear marcadores con relleno:

```python
fig, axs = plt.subplots(ncols=2)
fig.suptitle('Filled markers', fontsize=14)
for ax, markers in zip(axs, split_list(Line2D.filled_markers)):
    for y, marker in enumerate(markers):
        ax.text(-0.5, y, repr(marker), **text_style)
        ax.plot([y] * 3, marker=marker, **marker_style)
    format_axes(ax)
```
