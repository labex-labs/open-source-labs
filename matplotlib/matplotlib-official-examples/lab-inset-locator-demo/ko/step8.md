# Figure 좌표에서 중앙에 위치한 삽입 생성

`blended_transform_factory()` 메서드를 사용하여 혼합 변환 (blended transform) 을 생성하고 이를 `bbox_transform` 매개변수로 사용하여 figure 좌표에서 수평으로 중앙에 위치하고 축과 정렬되도록 수직으로 바인딩된 삽입을 생성할 수 있습니다.

```python
# figure 좌표에서 수평으로 중앙에 위치하고 축과 정렬되도록 수직으로 바인딩된 삽입 생성.
from matplotlib.transforms import blended_transform_factory

transform = blended_transform_factory(fig.transFigure, ax2.transAxes)
axins4 = inset_axes(ax2, width="16%", height="34%",
                    bbox_to_anchor=(0, 0, 1, 1),
                    bbox_transform=transform, loc=8, borderpad=0)
```
