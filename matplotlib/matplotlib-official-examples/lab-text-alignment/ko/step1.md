# 사각형 생성

`matplotlib.patches` 모듈의 `Rectangle()` 함수를 사용하여 플롯에 사각형을 생성하는 것으로 시작합니다. 사각형을 생성한 후, `set_xlim()` 및 `set_ylim()` 함수를 사용하여 가로 및 세로 범위를 설정합니다. 마지막으로, 사각형을 플롯에 추가합니다.

```python
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

fig, ax = plt.subplots()

# Build a rectangle in axes coords
left, width = .25, .5
bottom, height = .25, .5
right = left + width
top = bottom + height
p = Rectangle((left, bottom), width, height, fill=False)
ax.add_patch(p)

# Set the horizontal and vertical limits
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
plt.show()
```
