# App 클래스 정의

App 클래스는 애플리케이션을 생성하고 GUI 를 표시합니다.

```python
class App(wx.App):
    def OnInit(self):
        self.frame1 = FourierDemoFrame(parent=None, title="Fourier Demo",
                                       size=(640, 480))
        self.frame1.Show()
        return True
```
