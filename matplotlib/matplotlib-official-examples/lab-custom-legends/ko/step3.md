# 다양한 Matplotlib 객체를 사용한 사용자 정의 범례 구성

이 단계에서는 `Line2D` 및 `Patch`를 포함한 다양한 Matplotlib 객체를 사용하여 사용자 정의 범례를 생성합니다. 먼저, `matplotlib.patches` 모듈에서 `Patch` 클래스를 가져옵니다. 다음으로, 사용자 정의 속성을 가진 `Line2D` 및 `Patch` 객체 목록을 생성합니다. 마지막으로, 사용자 정의 객체와 해당 레이블로 `legend()`를 호출합니다.

```python
# Import Line2D and Patch classes
from matplotlib.lines import Line2D
from matplotlib.patches import Patch

# Create legend elements
legend_elements = [Line2D([0], [0], color='b', lw=4, label='Line'),
                   Line2D([0], [0], marker='o', color='w', label='Scatter',
                          markerfacecolor='g', markersize=15),
                   Patch(facecolor='orange', edgecolor='r',
                         label='Color Patch')]

# Plot data and generate custom legend
fig, ax = plt.subplots()
ax.legend(handles=legend_elements, loc='center')
```
