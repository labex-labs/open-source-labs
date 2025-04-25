# インタラクティビティを設定する

カーソルの下の三角形を更新するために、インタラクティビティを設定する必要があります。`motion_notify_event`を使用して、マウスがプロット上を移動したときを検出します。TriFinder オブジェクトを使用してカーソルの下の三角形を取得し、三角形の頂点でポリゴンを更新し、三角形のインデックスでプロットのタイトルを更新する`on_mouse_move()`関数を作成します。

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
