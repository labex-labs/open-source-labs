# アプリケーションを作成する

wx.App から継承する新しいクラスを作成します。このクラスはフレームを作成し、イベントループを開始します。

```python
class MyApp(wx.App):
    def OnInit(self):
        frame = CanvasFrame(None, "wxPython mathtext demo app")
        self.SetTopWindow(frame)
        frame.Show(True)
        return True
```
