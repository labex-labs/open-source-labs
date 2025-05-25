# 그림자 그리기

약간의 오프셋과 회색 색상을 사용하여 동일한 선에 대한 그림자를 그립니다. 원래 선 아래에 그림자 선이 그려지도록 그림자 선의 색상과 zorder 를 조정합니다. 또한 `offset_copy()` 메서드를 사용하여 그림자 선에 대한 오프셋 변환을 생성합니다.

```python
for l in [l1, l2]:
    xx = l.get_xdata()
    yy = l.get_ydata()
    shadow, = ax.plot(xx, yy)
    shadow.update_from(l)

    shadow.set_color("0.2")
    shadow.set_zorder(l.get_zorder() - 0.5)

    transform = mtransforms.offset_copy(l.get_transform(), fig1, x=4.0, y=-6.0, units='points')
    shadow.set_transform(transform)

    shadow.set_gid(l.get_label() + "_shadow")
```
