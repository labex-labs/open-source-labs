# 음영 영역 생성

`Polygon` 패치를 사용하여 음영 영역을 생성합니다. `linspace`와 1 단계에서 정의된 함수를 사용하여 영역에 대한 x 및 y 값을 생성합니다. 그런 다음, 영역의 정점을 튜플 목록으로 정의합니다. 마지막으로, `Polygon` 객체를 생성하고 `add_patch`를 사용하여 축에 추가합니다.

```python
from matplotlib.patches import Polygon

ix = np.linspace(a, b)
iy = func(ix)
verts = [(a, 0), *zip(ix, iy), (b, 0)]
poly = Polygon(verts, facecolor='0.9', edgecolor='0.5')
ax.add_patch(poly)
```
