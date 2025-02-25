# アプリケーションクラスの定義

App クラスは、アプリケーションを作成し、GUI を表示します。

```python
class App(wx.App):
    def OnInit(self):
        self.frame1 = FourierDemoFrame(parent=None, title="Fourier Demo",
                                       size=(640, 480))
        self.frame1.Show()
        return True
```
