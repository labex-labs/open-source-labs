# 슬라이더 (slider) 를 위한 콜백 함수 생성

사용자가 슬라이더를 사용하여 임계값 (threshold value) 을 변경할 때마다 호출될 콜백 함수 (callback function) 를 생성합니다. 이 함수는 이미지의 colormap 과 히스토그램의 수직선 위치를 업데이트합니다.

```python
def update(val):
    # The val passed to a callback by the RangeSlider will
    # be a tuple of (min, max)

    # Update the image's colormap
    im.norm.vmin = val[0]
    im.norm.vmax = val[1]

    # Update the position of the vertical lines
    lower_limit_line.set_xdata([val[0], val[0]])
    upper_limit_line.set_xdata([val[1], val[1]])

    # Redraw the figure to ensure it updates
    fig.canvas.draw_idle()


slider.on_changed(update)
```
