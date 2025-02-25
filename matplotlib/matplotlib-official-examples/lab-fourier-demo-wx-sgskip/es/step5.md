# Definir la clase App

La clase App creará la aplicación y mostrará la interfaz gráfica de usuario (GUI).

```python
class App(wx.App):
    def OnInit(self):
        self.frame1 = FourierDemoFrame(parent=None, title="Fourier Demo",
                                       size=(640, 480))
        self.frame1.Show()
        return True
```
