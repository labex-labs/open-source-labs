# App-Klasse definieren

Die App-Klasse wird die Anwendung erstellen und die grafische Benutzeroberfläche (GUI) anzeigen.

```python
class App(wx.App):
    def OnInit(self):
        self.frame1 = FourierDemoFrame(parent=None, title="Fourier Demo",
                                       size=(640, 480))
        self.frame1.Show()
        return True
```
