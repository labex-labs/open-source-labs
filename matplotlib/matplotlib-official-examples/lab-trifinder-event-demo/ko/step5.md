# 상호 작용 설정

커서 아래의 삼각형을 업데이트하기 위해 상호 작용을 설정해야 합니다. `motion_notify_event`를 사용하여 마우스가 플롯 위로 이동할 때를 감지합니다. `TriFinder` 객체를 사용하여 커서 아래의 삼각형을 가져오고, 삼각형의 꼭지점으로 polygon 을 업데이트하며, 삼각형의 인덱스로 플롯 제목을 업데이트하는 `on_mouse_move()` 함수를 생성합니다.

```python
def on_mouse_move(event):
    if event.inaxes is None:
        tri = -1
    else:
        tri = trifinder(event.xdata, event.ydata)
    update_polygon(tri)
    ax.set_title(f'Triangle {tri}')
    event.canvas.draw()

fig.canvas.mpl_connect('motion_notify_event', on_mouse_move)
```
