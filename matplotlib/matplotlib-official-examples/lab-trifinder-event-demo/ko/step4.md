# 커서 아래 삼각형 강조

마우스가 플롯 위로 이동할 때 커서 아래의 삼각형을 강조 표시하려고 합니다. 이를 위해 커서 아래의 삼각형의 꼭지점으로 업데이트될 `Polygon` 객체를 생성합니다. `ax.add_patch()`를 사용하여 플롯에 polygon 을 추가합니다.

```python
from matplotlib.patches import Polygon

polygon = Polygon([[0, 0], [0, 0], [0, 0]], facecolor='y')
ax.add_patch(polygon)
```

또한 커서 아래의 삼각형의 꼭지점으로 polygon 의 꼭지점을 업데이트하는 `update_polygon()` 함수를 생성합니다.

```python
def update_polygon(tri):
    if tri == -1:
        points = [0, 0, 0]
    else:
        points = triang.triangles[tri]
    xs = triang.x[points]
    ys = triang.y[points]
    polygon.set_xy(np.column_stack([xs, ys]))
```
