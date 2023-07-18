# Add a Toolbar

Add a toolbar to the application that allows the user to zoom in and out, pan, and save the plot as an image. This toolbar is added to the bottom of the frame.

```python
    def add_toolbar(self):
        self.toolbar = NavigationToolbar2Wx(self.canvas)
        self.toolbar.Realize()
        self.sizer.Add(self.toolbar, 0, wx.LEFT | wx.EXPAND)
        self.toolbar.update()
```
