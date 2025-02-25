# Создайте приложение

Создайте новый класс, наследующийся от wx.App. Этот класс создает рамку и запускает цикл событий.

```python
class MyApp(wx.App):
    def OnInit(self):
        frame = CanvasFrame(None, "wxPython mathtext demo app")
        self.SetTopWindow(frame)
        frame.Show(True)
        return True
```
