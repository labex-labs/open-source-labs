# カーソルを変更する

次に、キャンバスフレームにカーソルが入ったときにカーソルを変更するメソッドを定義します。この場合、カーソルをターゲットマークに変更します。

```python
def ChangeCursor(self, event):
    self.figure_canvas.SetCursor(wx.Cursor(wx.CURSOR_BULLSEYE))
```
