# Define a Custom Navigation Toolbar

Next, we define a custom navigation toolbar that extends the default wx toolbar with our own event handlers. In this case, we use a stock wx bitmap and add a custom control that adds text to the axes in a random location and color when clicked.

```python
class MyNavigationToolbar(NavigationToolbar):
    def __init__(self, canvas):
        super().__init__(canvas)
        bmp = wx.ArtProvider.GetBitmap(wx.ART_CROSS_MARK, wx.ART_TOOLBAR)
        tool = self.AddTool(wx.ID_ANY, 'Click me', bmp, 'Activate custom control')
        self.Bind(wx.EVT_TOOL, self._on_custom, id=tool.GetId())

    def _on_custom(self, event):
        ax = self.canvas.figure.axes[0]
        x, y = np.random.rand(2)
        rgb = np.random.rand(3)
        ax.text(x, y, 'You clicked me', transform=ax.transAxes, color=rgb)
        self.canvas.draw()
        event.Skip()
```
