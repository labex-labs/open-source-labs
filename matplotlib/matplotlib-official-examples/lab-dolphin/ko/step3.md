# 돌고래 모양 회전

`Affine2D().rotate_deg()` 함수를 사용하여 돌고래 모양을 60 도 회전시킵니다.

```python
from matplotlib.transforms import Affine2D

vertices = Affine2D().rotate_deg(60).transform(vertices)
dolphin_path2 = Path(vertices, codes)
dolphin_patch2 = PathPatch(dolphin_path2, facecolor=(0.5, 0.5, 0.5),
                           edgecolor=(0.0, 0.0, 0.0))
ax.add_patch(dolphin_patch2)
```
