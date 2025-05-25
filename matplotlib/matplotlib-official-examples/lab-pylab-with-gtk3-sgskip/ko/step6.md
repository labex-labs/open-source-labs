# 마우스 움직임에 따라 레이블 텍스트 업데이트

축 위로 마우스를 드래그할 때 마우스의 x, y 좌표를 표시하도록 레이블 텍스트를 업데이트합니다. 레이블 텍스트를 업데이트하는 함수를 생성하고, `mpl_connect()` 메서드를 사용하여 `motion_notify_event`에 연결합니다.

```python
def update(event):
    if event.xdata is None:
        label.set_markup('Drag mouse over axes for position')
    else:
        label.set_markup(
            f'<span color="#ef0000">x,y=({event.xdata}, {event.ydata})</span>')

fig.canvas.mpl_connect('motion_notify_event', update)
```
