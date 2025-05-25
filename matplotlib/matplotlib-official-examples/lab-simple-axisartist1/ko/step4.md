# Subplot 2 생성

두 번째 subplot 에서 `axisartist.axislines.AxesZero`를 사용하여 xzero 및 yzero 축을 자동으로 생성합니다. 다른 spine 들을 보이지 않게 하고 xzero 축을 보이도록 설정합니다.

```python
ax1 = fig.add_subplot(gs[0, 1], axes_class=axisartist.axislines.AxesZero)
ax1.axis["xzero"].set_visible(True)
ax1.axis["xzero"].label.set_text("Axis Zero")
ax1.axis["bottom", "top", "right"].set_visible(False)
```
