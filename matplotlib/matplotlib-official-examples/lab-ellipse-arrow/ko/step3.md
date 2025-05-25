# 방향 화살표 추가

타원의 단축 끝점에 마커를 플로팅하여 타원에 방향 화살표를 추가할 수 있습니다. `get_co_vertices()` 메서드를 사용하여 타원의 꼭지점 좌표를 얻을 수 있습니다. 그런 다음, `Affine2D()` 클래스를 사용하여 마커를 타원의 각도에 맞게 회전시킬 수 있습니다.

```python
from matplotlib.markers import MarkerStyle
from matplotlib.transforms import Affine2D

# Plot an arrow marker at the end point of minor axis
vertices = ellipse.get_co_vertices()
t = Affine2D().rotate_deg(ellipse.angle)
ax.plot(
    vertices[0][0],
    vertices[0][1],
    color="b",
    marker=MarkerStyle(">", "full", t),
    markersize=10
)
```
