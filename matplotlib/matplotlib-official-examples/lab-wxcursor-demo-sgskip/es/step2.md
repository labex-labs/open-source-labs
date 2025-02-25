# Cambiar el cursor

A continuación, definiremos un método para cambiar el cursor cuando ingrese al marco de lienzo. En este caso, cambiaremos el cursor a un objetivo.

```python
def ChangeCursor(self, event):
    self.figure_canvas.SetCursor(wx.Cursor(wx.CURSOR_BULLSEYE))
```
