# 커서 좌표로 레이블 업데이트

```python
def update(event):
    if event.xdata is None:
        label.set_markup('Drag mouse over axes for position')
    else:
        label.set_markup(
            f'<span color="#ef0000">x,y=({event.xdata}, {event.ydata})</span>')

fig.canvas.mpl_connect('motion_notify_event', update)
```

플롯 위에서 커서가 움직일 때 커서의 x 및 y 좌표로 레이블을 업데이트하는 함수를 생성합니다. 함수를 캔버스의 `motion_notify_event`에 연결합니다.
