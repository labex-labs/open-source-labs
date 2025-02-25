# Créer l'application

Créez une nouvelle classe qui hérite de wx.App. Cette classe crée le cadre et démarre la boucle d'événements.

```python
class MyApp(wx.App):
    def OnInit(self):
        frame = CanvasFrame(None, "wxPython mathtext demo app")
        self.SetTopWindow(frame)
        frame.Show(True)
        return True
```
