# 사용자 정의 범례 구성

이 단계에서는 Matplotlib 객체를 사용하여 사용자 정의 범례를 생성합니다. 먼저, `matplotlib.lines` 모듈에서 `Line2D` 클래스를 가져옵니다. 다음으로, 사용자 정의 색상, 너비 및 레이블 속성을 가진 `Line2D` 객체 목록을 생성합니다. 마지막으로, `plot` 함수를 사용하여 데이터를 다시 플롯하고 사용자 정의 선과 해당 레이블로 `legend()`를 호출합니다.

```python
# Import Line2D class
from matplotlib.lines import Line2D

# Create custom lines
custom_lines = [Line2D([0], [0], color=cmap(0.), lw=4),
                Line2D([0], [0], color=cmap(.5), lw=4),
                Line2D([0], [0], color=cmap(1.), lw=4)]

# Plot data and generate custom legend
fig, ax = plt.subplots()
lines = ax.plot(data)
ax.legend(custom_lines, ['Cold', 'Medium', 'Hot'])
```
