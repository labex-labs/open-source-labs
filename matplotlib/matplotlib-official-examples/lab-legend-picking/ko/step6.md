# On Pick 이벤트 함수 정의

범례 프록시 선에 해당하는 원래 선의 가시성을 토글하는 on pick 이벤트 함수를 정의합니다.

```python
def on_pick(event):
    # On the pick event, find the original line corresponding to the legend
    # proxy line, and toggle its visibility.
    legline = event.artist
    origline = lined[legline]
    visible = not origline.get_visible()
    origline.set_visible(visible)
    # Change the alpha on the line in the legend, so we can see what lines
    # have been toggled.
    legline.set_alpha(1.0 if visible else 0.2)
    fig.canvas.draw()
```
