# 플로팅 축 생성

이 단계에서는 직사각형 상자에 극좌표 곡선을 표시하는 데 사용될 두 개의 플로팅 축을 생성합니다. `new_floating_axis()`를 사용하여 플로팅 축을 생성합니다.

```python
# Create the floating axes
ax1.axis["lat"] = axis = ax1.new_floating_axis(0, 60)
axis.label.set_text(r"$\theta = 60^{\circ}$")
axis.label.set_visible(True)

ax1.axis["lon"] = axis = ax1.new_floating_axis(1, 6)
axis.label.set_text(r"$r = 6$")
```
