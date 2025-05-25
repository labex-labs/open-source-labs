# 플롯 설정

먼저, 두 개의 서브플롯 (subplots) 으로 플롯을 설정해야 합니다. `subplots` 함수를 사용하여 2x2 그리드의 서브플롯을 생성한 다음, 두 점의 x 및 y 좌표를 정의합니다.

```python
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

fig, axs = plt.subplots(2, 2)
x1, y1 = 0.3, 0.3
x2, y2 = 0.7, 0.7
```
