# 텍스트 포인트 및 주석 포인트 지정

이 점에 주석을 달려면 주석 포인트 `xy=(x, y)`를 지정해야 합니다. 또한, 이 주석에 대한 텍스트 위치에 대한 텍스트 포인트 `xytext=(x, y)`를 지정할 수 있습니다. 선택적으로, `xycoords` 및 `textcoords`에 대해 다음 문자열 중 하나를 사용하여 `xy` 및 `xytext`의 좌표계를 지정할 수 있습니다 (기본값은 'data'입니다).

- 'figure points' : 그림의 왼쪽 하단 모서리에서 점
- 'figure pixels' : 그림의 왼쪽 하단 모서리에서 픽셀
- 'figure fraction' : (0, 0) 은 그림의 왼쪽 하단이고 (1, 1) 은 오른쪽 상단입니다.
- 'axes points' : 축의 왼쪽 하단 모서리에서 점
- 'axes pixels' : 축의 왼쪽 하단 모서리에서 픽셀
- 'axes fraction' : (0, 0) 은 축의 왼쪽 하단이고 (1, 1) 은 오른쪽 상단입니다.
- 'offset points' : `xy` 값에서 오프셋 (포인트) 을 지정합니다.
- 'offset pixels' : `xy` 값에서 오프셋 (픽셀) 을 지정합니다.
- 'data' : 축 데이터 좌표계를 사용합니다.

참고: 물리적 좌표계 (점 또는 픽셀) 의 경우 원점은 그림 또는 축의 (아래쪽, 왼쪽) 입니다.

선택적으로, 화살표 속성을 지정하여 텍스트에서 주석이 달린 점까지 화살표를 그릴 수 있습니다. 화살표 속성의 딕셔너리를 제공합니다. 유효한 키는 다음과 같습니다.

- `width`: 포인트 단위의 화살표 너비
- `frac`: 머리가 차지하는 화살표 길이의 비율
- `headwidth`: 포인트 단위의 화살표 머리 밑면 너비
- `shrink`: 주석이 달린 점과 텍스트에서 팁과 밑면을 몇 퍼센트 이동합니다.
- `any key for matplotlib.patches.polygon` (예: facecolor)

```python
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.patches import Ellipse
from matplotlib.text import OffsetFrom

# Create our figure and data we'll use for plotting
fig, ax = plt.subplots(figsize=(4, 4))

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)

# Plot a line and add some simple annotations
line, = ax.plot(t, s)
ax.annotate('figure pixels',
            xy=(10, 10), xycoords='figure pixels')
ax.annotate('figure points',
            xy=(107, 110), xycoords='figure points',
            fontsize=12)
ax.annotate('figure fraction',
            xy=(.025, .975), xycoords='figure fraction',
            horizontalalignment='left', verticalalignment='top',
            fontsize=20)

# The following examples show off how these arrows are drawn.

ax.annotate('point offset from data',
            xy=(3, 1), xycoords='data',
            xytext=(-10, 90), textcoords='offset points',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='center', verticalalignment='bottom')

ax.annotate('axes fraction',
            xy=(2, 1), xycoords='data',
            xytext=(0.36, 0.68), textcoords='axes fraction',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='right', verticalalignment='top')

# You may also use negative points or pixels to specify from (right, top).
# E.g., (-10, 10) is 10 points to the left of the right side of the axes and 10
# points above the bottom

ax.annotate('pixel offset from axes fraction',
            xy=(1, 0), xycoords='axes fraction',
            xytext=(-20, 20), textcoords='offset pixels',
            horizontalalignment='right',
            verticalalignment='bottom')

ax.set(xlim=(-1, 5), ylim=(-3, 5))
```
