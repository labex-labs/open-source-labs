# 마우스 이동 이벤트

`motion_notify_event` 메서드를 사용하여 마우스 이동 이벤트에 연결할 수 있습니다. 이 예제에서는 마우스가 플롯 위로 이동할 때 x 및 y 데이터 좌표와 x 및 y 픽셀 좌표를 출력합니다.

```python
def on_move(event):
    if event.inaxes:
        print(f'data coords {event.xdata} {event.ydata},',
              f'pixel coords {event.x} {event.y}')

binding_id = plt.connect('motion_notify_event', on_move)
```
