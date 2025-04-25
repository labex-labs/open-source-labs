# 创建应用程序

创建一个继承自 wx.App 的新类。这个类创建框架并启动事件循环。

```python
class MyApp(wx.App):
    def OnInit(self):
        frame = CanvasFrame(None, "wxPython mathtext demo app")
        self.SetTopWindow(frame)
        frame.Show(True)
        return True
```
