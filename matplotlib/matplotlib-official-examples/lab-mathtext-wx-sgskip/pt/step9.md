# Criar a Aplicação

Crie uma nova classe que herda de `wx.App`. Esta classe cria o frame e inicia o loop de eventos.

```python
class MyApp(wx.App):
    def OnInit(self):
        frame = CanvasFrame(None, "wxPython mathtext demo app")
        self.SetTopWindow(frame)
        frame.Show(True)
        return True
```
