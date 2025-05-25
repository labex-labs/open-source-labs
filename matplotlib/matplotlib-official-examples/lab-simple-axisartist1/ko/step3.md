# Subplot 1 생성

첫 번째 subplot 에서 `axisartist.Axes`를 사용하여 y=0 을 통과하는 새로운 축을 생성합니다. 또한 다른 spine 들을 보이지 않게 만듭니다.

```python
ax0 = fig.add_subplot(gs[0, 0], axes_class=axisartist.Axes)
ax0.axis["y=0"] = ax0.new_floating_axis(nth_coord=0, value=0, axis_direction="bottom")
ax0.axis["y=0"].toggle(all=True)
ax0.axis["y=0"].label.set_text("y = 0")
ax0.axis["bottom", "top", "right"].set_visible(False)
```
