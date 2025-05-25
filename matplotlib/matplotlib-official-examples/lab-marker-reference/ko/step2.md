# 채워진 마커 (Filled Markers)

채워진 마커는 채워지지 않은 마커의 반대입니다. 다음 코드는 채워진 마커를 만드는 방법을 보여줍니다.

```python
fig, axs = plt.subplots(ncols=2)
fig.suptitle('Filled markers', fontsize=14)
for ax, markers in zip(axs, split_list(Line2D.filled_markers)):
    for y, marker in enumerate(markers):
        ax.text(-0.5, y, repr(marker), **text_style)
        ax.plot([y] * 3, marker=marker, **marker_style)
    format_axes(ax)
```
