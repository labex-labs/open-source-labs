# カーソル座標でラベルを更新する

```python
def update(event):
    if event.xdata is None:
        label.set_markup('Drag mouse over axes for position')
    else:
        label.set_markup(
            f'<span color="#ef0000">x,y=({event.xdata}, {event.ydata})</span>')

fig.canvas.mpl_connect('motion_notify_event', update)
```

プロット上をカーソルが移動したときに、その x 座標と y 座標でラベルを更新する関数を作成します。この関数をキャンバスの `motion_notify_event` に接続します。
