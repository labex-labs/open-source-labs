# 세 점을 클릭하여 삼각형 정의하기

이 단계에서는 세 점을 클릭하여 삼각형을 정의합니다. 이를 위해 `ginput` 및 `waitforbuttonpress` 함수를 사용합니다. `ginput` 함수를 사용하면 마우스로 플롯에서 점을 선택할 수 있으며, `waitforbuttonpress` 함수는 버튼 누름 이벤트를 기다립니다.

```python
import time
import matplotlib.pyplot as plt
import numpy as np

def tellme(s):
    print(s)
    plt.title(s, fontsize=16)
    plt.draw()

plt.figure()
plt.xlim(0, 1)
plt.ylim(0, 1)

tellme('You will define a triangle, click to begin')

plt.waitforbuttonpress()

while True:
    pts = []
    while len(pts) < 3:
        tellme('Select 3 corners with mouse')
        pts = np.asarray(plt.ginput(3, timeout=-1))
        if len(pts) < 3:
            tellme('Too few points, starting over')
            time.sleep(1)  # Wait a second

    ph = plt.fill(pts[:, 0], pts[:, 1], 'r', lw=2)

    tellme('Happy? Key click for yes, mouse click for no')

    if plt.waitforbuttonpress():
        break

    # Get rid of fill
    for p in ph:
        p.remove()
```
