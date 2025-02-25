# Changer le curseur

Ensuite, nous allons définir une méthode pour changer le curseur lorsqu'il entre dans la trame de canevas. Dans ce cas, nous changerons le curseur en un pointillé.

```python
def ChangeCursor(self, event):
    self.figure_canvas.SetCursor(wx.Cursor(wx.CURSOR_BULLSEYE))
```
