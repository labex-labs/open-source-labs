# Измените курсор

Далее мы определим метод для изменения курсора, когда он входит в рамку холста. В этом случае мы изменим курсор на мишень.

```python
def ChangeCursor(self, event):
    self.figure_canvas.SetCursor(wx.Cursor(wx.CURSOR_BULLSEYE))
```
