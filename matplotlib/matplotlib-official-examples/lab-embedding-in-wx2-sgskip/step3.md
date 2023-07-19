# Create the Application

The next step is to create the application by inheriting from wx.App. In the OnInit method, a CanvasFrame object is created and shown.

```python
class App(wx.App):
    def OnInit(self):
        self.Init()
        frame = CanvasFrame()
        frame.Show(True)

        return True
```
