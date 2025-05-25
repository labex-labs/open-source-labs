# 채워지지 않은 마커 (Unfilled Markers)

채워지지 않은 마커는 단색입니다. 다음 코드는 채워지지 않은 마커를 만드는 방법을 보여줍니다.

```python
unfilled_markers = [m for m, func in Line2D.markers.items()
                    if func != 'nothing' and m not in Line2D.filled_markers]

for ax, markers in zip(axs, split_list(unfilled_markers)):
    for y, marker in enumerate(markers):
        ax.text(-0.5, y, repr(marker), **text_style)
        ax.plot([y] * 3, marker=marker, **marker_style)
    format_axes(ax)
```
