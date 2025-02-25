# Ändern des Cursors

Als nächstes werden wir eine Methode definieren, um den Cursor zu ändern, wenn er den Canvas-Frame betritt. In diesem Fall werden wir den Cursor in einen Kreiszeiger umwandeln.

```python
def ChangeCursor(self, event):
    self.figure_canvas.SetCursor(wx.Cursor(wx.CURSOR_BULLSEYE))
```
