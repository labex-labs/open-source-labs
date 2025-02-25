# Définition de la classe App

La classe App créera l'application et affichera l'interface graphique utilisateur (GUI).

```python
class App(wx.App):
    def OnInit(self):
        self.frame1 = FourierDemoFrame(parent=None, title="Fourier Demo",
                                       size=(640, 480))
        self.frame1.Show()
        return True
```
