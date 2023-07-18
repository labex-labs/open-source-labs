# Matplotlib Tutorial: Creating a Custom Toolbar in wxPython

## Introduction

In this lab, we will learn how to create a custom toolbar in a wxPython application using Matplotlib. The toolbar will have a custom control that adds text to the axes in a random location and color when clicked.

## Steps

### Step 1: Import Libraries

First, we need to import the necessary libraries - wx, numpy, Matplotlib's FigureCanvasWxAgg, and NavigationToolbar2WxAgg.

```python
import wx
import numpy as np
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wxagg import NavigationToolbar2WxAgg as NavigationToolbar
from matplotlib.figure import Figure
```

### Step 2: Define a Custom Navigation Toolbar

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

### Step 3: Define a CanvasFrame Class

We then define a CanvasFrame class that creates a figure, adds a subplot to it, plots a sine wave, and creates a canvas to display the plot. We also create a sizer and add the canvas and custom toolbar to it.

```python
class CanvasFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, -1, 'CanvasFrame', size=(550, 350))

        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.axes = self.figure.add_subplot()
        t = np.arange(0.0, 3.0, 0.01)
        s = np.sin(2 * np.pi * t)

        self.axes.plot(t, s)

        self.canvas = FigureCanvas(self, -1, self.figure)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas, 1, wx.TOP | wx.LEFT | wx.EXPAND)

        self.toolbar = MyNavigationToolbar(self.canvas)
        self.toolbar.Realize()
        self.sizer.Add(self.toolbar, 0, wx.LEFT | wx.EXPAND)

        self.toolbar.update()
        self.SetSizer(self.sizer)
        self.Fit()
```

### Step 4: Create the Application

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

## Summary

In this lab, we learned how to create a custom toolbar in a wxPython application using Matplotlib. We created a custom navigation toolbar with a control that adds text to the axes in a random location and color when clicked. We also defined a CanvasFrame class that created a figure, added a subplot, and displayed the plot on a canvas with the custom toolbar. Finally, we created the application and inserted the custom frame into the main window.
