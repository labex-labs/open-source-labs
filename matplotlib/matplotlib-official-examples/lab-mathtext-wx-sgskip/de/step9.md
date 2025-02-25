# Erstellen der Anwendung

Erstellen Sie eine neue Klasse, die von wx.App erbt. Diese Klasse erstellt das Fenster und startet die Ereignisschleife.

```python
class MyApp(wx.App):
    def OnInit(self):
        frame = CanvasFrame(None, "wxPython mathtext demo app")
        self.SetTopWindow(frame)
        frame.Show(True)
        return True
```
