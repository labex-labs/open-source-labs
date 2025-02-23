# 描画イベントをコールバック関数に接続する

`draw_event` を `on_draw` 関数に接続する必要があります。

```python
fig.canvas.mpl_connect('draw_event', on_draw)
```
