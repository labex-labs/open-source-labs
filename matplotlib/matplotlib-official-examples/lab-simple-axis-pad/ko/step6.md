# 눈금 위치 조정

이 단계에서는 부동 축의 눈금 위치를 조정합니다. 이는 `major_ticks` 객체의 `tick_out` 속성을 `True`로 설정하여 수행할 수 있습니다.

```python
# Adjust Tick Position
fig = plt.figure(figsize=(9, 3.))
fig.subplots_adjust(left=0.01, right=0.99, bottom=0.01, top=0.99, wspace=0.01, hspace=0.01)

ax1 = setup_axes(fig, rect=121)
axis = add_floating_axis(ax1)

ax1 = setup_axes(fig, rect=122)
axis = add_floating_axis(ax1)
axis.major_ticks.set_tick_out(True)

plt.show()
```
