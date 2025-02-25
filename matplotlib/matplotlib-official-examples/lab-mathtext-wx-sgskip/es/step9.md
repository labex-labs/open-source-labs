# Crear la aplicación

Crea una nueva clase que herede de wx.App. Esta clase crea el marco y comienza el bucle de eventos.

```python
class MyApp(wx.App):
    def OnInit(self):
        frame = CanvasFrame(None, "wxPython mathtext demo app")
        self.SetTopWindow(frame)
        frame.Show(True)
        return True
```
