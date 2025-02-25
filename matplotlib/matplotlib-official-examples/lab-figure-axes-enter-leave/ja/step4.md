# イベントハンドラを図のキャンバスに接続する

ここでは、`mpl_connect`メソッドを使ってイベントハンドラを図のキャンバスに接続します。これにより、マウスが図または軸に入ったり離れたりするときにイベントハンドラがトリガーされるようになります。

```python
fig.canvas.mpl_connect('figure_enter_event', on_enter_figure)
fig.canvas.mpl_connect('figure_leave_event', on_leave_figure)
fig.canvas.mpl_connect('axes_enter_event', on_enter_axes)
fig.canvas.mpl_connect('axes_leave_event', on_leave_axes)
```
