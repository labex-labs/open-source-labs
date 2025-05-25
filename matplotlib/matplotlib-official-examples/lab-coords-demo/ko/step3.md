# 마우스 클릭 이벤트

`button_press_event` 메서드를 사용하여 마우스 클릭 이벤트에 연결할 수 있습니다. 이 예제에서는 왼쪽 마우스 버튼을 클릭하면 마우스 이동 이벤트 콜백을 연결 해제합니다.

```python
from matplotlib.backend_bases import MouseButton

def on_click(event):
    if event.button is MouseButton.LEFT:
        print('disconnecting callback')
        plt.disconnect(binding_id)

plt.connect('button_press_event', on_click)
```
