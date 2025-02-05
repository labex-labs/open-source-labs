# 更改光标

接下来，我们将定义一个方法，以便在光标进入画布框架时更改光标。在这种情况下，我们将把光标更改为靶心形状。

```python
def ChangeCursor(self, event):
    self.figure_canvas.SetCursor(wx.Cursor(wx.CURSOR_BULLSEYE))
```
