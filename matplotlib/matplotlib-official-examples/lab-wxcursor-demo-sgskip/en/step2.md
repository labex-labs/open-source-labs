# Change the Cursor

Next, we will define a method to change the cursor when it enters the canvas frame. In this case, we will change the cursor to a bullseye.

```python
def ChangeCursor(self, event):
    self.figure_canvas.SetCursor(wx.Cursor(wx.CURSOR_BULLSEYE))
```
