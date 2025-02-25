# マウスクリックイベント

`button_press_event` メソッドを使って、マウスクリックイベントに接続することができます。この例では、左マウスボタンがクリックされたときにマウス移動イベントのコールバックを切断しています。

```python
from matplotlib.backend_bases import MouseButton

def on_click(event):
    if event.button is MouseButton.LEFT:
        print('disconnecting callback')
        plt.disconnect(binding_id)

plt.connect('button_press_event', on_click)
```
