# マウス移動時にラベルのテキストを更新する

マウスを軸の上をドラッグしたときのx,y座標を表示するために、ラベルのテキストを更新します。ラベルのテキストを更新する関数を作成し、`mpl_connect()` メソッドを使って `motion_notify_event` に接続します。

```python
def update(event):
    if event.xdata is None:
        label.set_markup('Drag mouse over axes for position')
    else:
        label.set_markup(
            f'<span color="#ef0000">x,y=({event.xdata}, {event.ydata})</span>')

fig.canvas.mpl_connect('motion_notify_event', update)
```
