# Определение класса App

Класс App создаст приложение и отобразит графический интерфейс пользователя (GUI).

```python
class App(wx.App):
    def OnInit(self):
        self.frame1 = FourierDemoFrame(parent=None, title="Fourier Demo",
                                       size=(640, 480))
        self.frame1.Show()
        return True
```
