# Create the Application

Finally, we create the application and insert the custom frame into the main window.

```python
class App(wx.App):
    def OnInit(self):
        frame = CanvasFrame()
        frame.Show(True)
        return True

if __name__ == "__main__":
    app = App()
    app.MainLoop()
```
