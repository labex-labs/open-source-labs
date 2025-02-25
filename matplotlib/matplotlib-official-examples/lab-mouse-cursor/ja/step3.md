# マウスオーバー時にカーソルを設定する

ユーザーがサブプロットの上にマウスオーバーしたときに、代替カーソルにカーソルを設定する必要があります。これは、`motion_notify_event` イベントと `set_cursor()` 関数を使って達成します。

```python
def hover(event):
    if fig.canvas.widgetlock.locked():
        # Don't do anything if the zoom/pan tools have been enabled.
        return

    fig.canvas.set_cursor(
        event.inaxes.cursor_to_use if event.inaxes else Cursors.POINTER)

fig.canvas.mpl_connect('motion_notify_event', hover)
```
