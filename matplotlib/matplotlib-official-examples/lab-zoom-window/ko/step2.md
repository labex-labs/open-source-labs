# on_press 함수 정의

다음으로, 첫 번째 창에서 마우스 클릭 위치를 기반으로 두 번째 창의 x 및 y 제한을 조정하는 `on_press`라는 함수를 정의합니다.

```python
def on_press(event):
    if event.button != 1:
        return
    x, y = event.xdata, event.ydata
    axzoom.set_xlim(x - 0.1, x + 0.1)
    axzoom.set_ylim(y - 0.1, y + 0.1)
    figzoom.canvas.draw()
```
