# 함수로 사용자 정의 박스 스타일 구현하기

사용자 정의 박스 스타일은 사각형 박스와 "변형 (mutation)"의 양을 모두 지정하는 인수를 취하고 "변형된 (mutated)" 경로를 반환하는 함수로 구현할 수 있습니다. 여기서는 박스 왼쪽에 "화살표" 모양을 추가하는 새로운 경로를 반환하는 사용자 정의 박스 스타일을 구현합니다.

```python
import matplotlib.pyplot as plt
from matplotlib.patches import BoxStyle
from matplotlib.path import Path

def custom_box_style(x0, y0, width, height, mutation_size):
    """
    박스의 위치와 크기가 주어지면, 그 주변의 박스 경로를 반환합니다.

    회전은 자동으로 처리됩니다.

    Parameters
    ----------
    x0, y0, width, height : float
        박스 위치 및 크기.
    mutation_size : float
        변형 참조 스케일, 일반적으로 텍스트 글꼴 크기.
    """
    # 패딩
    mypad = 0.3
    pad = mutation_size * mypad
    # 패딩이 추가된 너비와 높이.
    width = width + 2 * pad
    height = height + 2 * pad
    # 패딩된 박스의 경계
    x0, y0 = x0 - pad, y0 - pad
    x1, y1 = x0 + width, y0 + height
    # 새로운 경로 반환
    return Path([(x0, y0),
                 (x1, y0), (x1, y1), (x0, y1),
                 (x0-pad, (y0+y1)/2), (x0, y0),
                 (x0, y0)],
                closed=True)

fig, ax = plt.subplots(figsize=(3, 3))
ax.text(0.5, 0.5, "Test", size=30, va="center", ha="center", rotation=30,
        bbox=dict(boxstyle=custom_box_style, alpha=0.2))
plt.show()
```
