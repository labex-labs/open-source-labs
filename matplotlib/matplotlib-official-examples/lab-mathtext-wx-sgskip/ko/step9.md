# 애플리케이션 생성

wx.App 에서 상속받는 새로운 클래스를 생성합니다. 이 클래스는 프레임을 생성하고 이벤트 루프를 시작합니다.

```python
class MyApp(wx.App):
    def OnInit(self):
        frame = CanvasFrame(None, "wxPython mathtext demo app")
        self.SetTopWindow(frame)
        frame.Show(True)
        return True
```
