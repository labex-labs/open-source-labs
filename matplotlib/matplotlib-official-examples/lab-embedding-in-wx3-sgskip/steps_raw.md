# Python Matplotlib Tutorial: Creating a Plot Panel with WX

## Introduction

Matplotlib is a powerful library for creating visualizations in Python. In this tutorial, we will walk through the steps of creating a plot panel with WX, a popular GUI toolkit for Python.

## Steps

### Step 1: Install Dependencies

Before we start, make sure that you have Matplotlib and WX installed. You can install them using pip:

```python
pip install matplotlib wxpython
```

### Step 2: Import Libraries

We need to import the necessary libraries for creating the plot panel. We will use `wx`, `numpy`, `matplotlib`, and `matplotlib.cm`.

```python
import wx
import numpy as np
import matplotlib.cm as cm
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import (
    FigureCanvasWxAgg as FigureCanvas,
    NavigationToolbar2WxAgg as NavigationToolbar)
```

### Step 3: Create a Plot Panel Class

We will create a `PlotPanel` class that inherits from `wx.Panel`. The `__init__` method sets up the figure, canvas, and toolbar.

```python
class PlotPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent, -1)

        self.fig = Figure((5, 4), 75)
        self.canvas = FigureCanvas(self, -1, self.fig)
        self.toolbar = NavigationToolbar(self.canvas)
        self.toolbar.Realize()

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
        sizer.Add(self.toolbar, 0, wx.GROW)
        self.SetSizer(sizer)
        self.Fit()
```

### Step 4: Initialize Plot Data

We will create a method `init_plot_data` that initializes the plot data. This method sets up the subplot, generates the `x` and `y` data, and creates the image and lines.

```python
    def init_plot_data(self):
        ax = self.fig.add_subplot()

        x = np.arange(120.0) * 2 * np.pi / 60.0
        y = np.arange(100.0) * 2 * np.pi / 50.0
        self.x, self.y = np.meshgrid(x, y)
        z = np.sin(self.x) + np.cos(self.y)
        self.im = ax.imshow(z, cmap=cm.RdBu, origin='lower')

        zmax = np.max(z) - ERR_TOL
        ymax_i, xmax_i = np.nonzero(z >= zmax)
        if self.im.origin == 'upper':
            ymax_i = z.shape[0] - ymax_i
        self.lines = ax.plot(xmax_i, ymax_i, 'ko')

        self.toolbar.update()
```

### Step 5: Create Main App Class

We will create a main app class that inherits from `wx.App`. In the `OnInit` method, we will load the XRC file, create a panel, and create a plot container.

```python
class MyApp(wx.App):
    def OnInit(self):
        xrcfile = cbook.get_sample_data('embedding_in_wx3.xrc', asfileobj=False)
        self.res = xrc.XmlResource(xrcfile)

        self.frame = self.res.LoadFrame(None, "MainFrame")
        self.panel = xrc.XRCCTRL(self.frame, "MainPanel")

        plot_container = xrc.XRCCTRL(self.frame, "plot_container_panel")
        sizer = wx.BoxSizer(wx.VERTICAL)

        self.plotpanel = PlotPanel(plot_container)
        self.plotpanel.init_plot_data()

        sizer.Add(self.plotpanel, 1, wx.EXPAND)
        plot_container.SetSizer(sizer)

        whiz_button = xrc.XRCCTRL(self.frame, "whiz_button")
        whiz_button.Bind(wx.EVT_BUTTON, self.plotpanel.OnWhiz)

        bang_button = xrc.XRCCTRL(self.frame, "bang_button")
        bang_button.Bind(wx.EVT_BUTTON, self.OnBang)

        self.frame.Show()
        self.SetTopWindow(self.frame)

        return True
```

### Step 6: Update the Plot

We will create a method `OnWhiz` that updates the plot when the "Whiz" button is clicked. This method updates the `x`, `y`, and `z` data, and then updates the image and lines.

```python
    def OnWhiz(self, event):
        self.x += np.pi / 15
        self.y += np.pi / 20
        z = np.sin(self.x) + np.cos(self.y)
        self.im.set_array(z)

        zmax = np.max(z) - ERR_TOL
        ymax_i, xmax_i = np.nonzero(z >= zmax)
        if self.im.origin == 'upper':
            ymax_i = z.shape[0] - ymax_i
        self.lines[0].set_data(xmax_i, ymax_i)

        self.canvas.draw()
```

### Step 7: Update the Counter

We will create a method `OnBang` that updates the counter when the "Bang" button is clicked.

```python
    def OnBang(self, event):
        bang_count = xrc.XRCCTRL(self.frame, "bang_count")
        bangs = bang_count.GetValue()
        bangs = int(bangs) + 1
        bang_count.SetValue(str(bangs))
```

### Step 8: Run the App

We will create an instance of `MyApp` and run the app.

```python
if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()
```

## Summary

In this tutorial, we learned how to create a plot panel with WX and Matplotlib. We created a `PlotPanel` class, initialized the plot data, and updated the plot when the user clicked the "Whiz" button. We also updated a counter when the user clicked the "Bang" button.
