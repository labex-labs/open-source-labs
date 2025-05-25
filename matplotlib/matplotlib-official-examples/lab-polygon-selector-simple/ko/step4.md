# 모든 것을 함께 묶기

프로그래밍 방식과 대화형 방식으로 다각형을 생성하는 두 가지 방법을 모두 포함하는 완전한 예제를 만들어 보겠습니다.

```python
import matplotlib.pyplot as plt
from matplotlib.widgets import PolygonSelector

# Create a figure and axes
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(10, 5))

# Create a PolygonSelector object and add vertices
selector1 = PolygonSelector(ax1, lambda *args: None)
selector1.verts = [(0.1, 0.4), (0.5, 0.9), (0.3, 0.2)]

# Plot the polygon
ax1.add_patch(plt.Polygon(selector1.verts, alpha=0.3))

# Create another PolygonSelector object for interactive creation
selector2 = PolygonSelector(ax2, lambda *args: None)

print("다각형을 생성하려면 그림을 클릭하십시오.")
print("'esc' 키를 눌러 새 다각형을 시작하십시오.")
print("모든 정점을 이동하려면 'shift' 키를 누르고 시도하십시오.")
print("단일 정점을 이동하려면 'ctrl' 키를 누르고 시도하십시오.")

plt.show()
```
