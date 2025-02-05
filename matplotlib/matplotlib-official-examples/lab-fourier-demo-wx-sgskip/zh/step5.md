# 定义应用程序类

应用程序类将创建应用程序并显示图形用户界面（GUI）。

```python
class App(wx.App):
    def OnInit(self):
        self.frame1 = FourierDemoFrame(parent=None, title="Fourier Demo",
                                       size=(640, 480))
        self.frame1.Show()
        return True
```
