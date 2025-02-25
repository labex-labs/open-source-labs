# マウス移動イベント

`motion_notify_event` メソッドを使って、マウス移動イベントに接続することができます。この例では、マウスがプロット上を移動したときの x と y のデータ座標と x と y のピクセル座標を表示しています。

```python
def on_move(event):
    if event.inaxes:
        print(f'data coords {event.xdata} {event.ydata},',
              f'pixel coords {event.x} {event.y}')

binding_id = plt.connect('motion_notify_event', on_move)
```
