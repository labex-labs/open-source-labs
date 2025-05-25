# Mudar o Cursor

Em seguida, definiremos um método para mudar o cursor quando ele entrar no canvas frame. Neste caso, mudaremos o cursor para um alvo (bullseye).

```python
def ChangeCursor(self, event):
    self.figure_canvas.SetCursor(wx.Cursor(wx.CURSOR_BULLSEYE))
```
