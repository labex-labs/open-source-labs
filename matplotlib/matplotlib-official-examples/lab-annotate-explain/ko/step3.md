# 플롯에 타원 추가

이 단계에서는 플롯에 타원을 추가합니다. `Ellipse` 함수를 사용하여 타원을 생성하고, 위치, 너비, 높이 및 각도와 같은 타원 속성을 사용자 정의합니다.

```python
ax = axs.flat[1]
ax.plot([x1, x2], [y1, y2], ".")
el = mpatches.Ellipse((x1, y1), 0.3, 0.4, angle=30, alpha=0.2)
ax.add_artist(el)
```
