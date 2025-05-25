# 타원 생성

다음으로, `Ellipse` 클래스를 사용하여 타원을 생성해야 합니다. 타원의 중심, 타원의 너비와 높이, 회전 각도를 지정할 수 있습니다.

```python
from matplotlib.patches import Ellipse

ellipse = Ellipse(
    xy=(2, 4),
    width=30,
    height=20,
    angle=35,
    facecolor="none",
    edgecolor="b"
)
ax.add_patch(ellipse)
```
