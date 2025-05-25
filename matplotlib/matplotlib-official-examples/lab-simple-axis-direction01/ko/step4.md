# 축 레이블 설정

`ax1.axis[]` 함수를 사용하여 플롯의 왼쪽 및 오른쪽 축 레이블을 설정합니다. 또한 `set_axis_direction()` 함수를 사용하여 눈금 레이블의 방향을 설정합니다.

```python
ax1.axis["left"].major_ticklabels.set_axis_direction("top")
ax1.axis["left"].label.set_text("Left label")

ax1.axis["right"].label.set_visible(True)
ax1.axis["right"].label.set_text("Right label")
ax1.axis["right"].label.set_axis_direction("left")
```
