# Add a Toolbar

To add a toolbar, a NavigationToolbar2WxAgg object is created and added to the CanvasFrame using a sizer. The update() method of the toolbar is then called to update the axes menu.

```python
    def add_toolbar(self):
        self.toolbar = NavigationToolbar(self.canvas)
        self.toolbar.Realize()
        self.sizer.Add(self.toolbar, 0, wx.LEFT | wx.EXPAND)
        self.toolbar.update()
```
