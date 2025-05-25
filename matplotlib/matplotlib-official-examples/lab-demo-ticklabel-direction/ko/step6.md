# 한쪽 면에서 바깥쪽을 가리키는 눈금 레이블

이 단계에서는 한쪽 면에서 바깥쪽을 가리키는 눈금 레이블을 가진 서브플롯을 생성합니다.

```python
ax = setup_axes(fig, 133)
ax.axis["left"].set_axis_direction("right")
ax.axis[:].major_ticks.set_tick_out(True)

ax.axis["left"].label.set_text("Long Label Left")
ax.axis["bottom"].label.set_text("Label Bottom")
ax.axis["right"].label.set_text("Long Label Right")
ax.axis["right"].label.set_visible(True)
ax.axis["left"].label.set_pad(0)
ax.axis["bottom"].label.set_pad(10)

plt.show()
```
