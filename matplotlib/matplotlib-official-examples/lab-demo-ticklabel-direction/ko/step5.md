# 사용자 정의 눈금 레이블 방향

이 단계에서는 사용자 정의된 눈금 레이블 방향을 가진 서브플롯을 생성합니다.

```python
ax = setup_axes(fig, 132)
ax.axis["left"].set_axis_direction("right")
ax.axis["bottom"].set_axis_direction("top")
ax.axis["right"].set_axis_direction("left")
ax.axis["top"].set_axis_direction("bottom")
```
