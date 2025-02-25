# Marcadores sin relleno

Los marcadores sin relleno son de un solo color. El siguiente código demuestra cómo crear marcadores sin relleno:

```python
unfilled_markers = [m for m, func in Line2D.markers.items()
                    if func!= 'nothing' and m not in Line2D.filled_markers]

for ax, markers in zip(axs, split_list(unfilled_markers)):
    for y, marker in enumerate(markers):
        ax.text(-0.5, y, repr(marker), **text_style)
        ax.plot([y] * 3, marker=marker, **marker_style)
    format_axes(ax)
```
