# Python Matplotlib Tutorial

## Introduction

This lab will guide you step-by-step through the process of using Python Matplotlib to create a simple graph using wxagg in an application with a toolbar.

## Steps

### Step 1: Create a CanvasFrame

The first step is to create a CanvasFrame which will contain the graph. The CanvasFrame is created by inheriting from wx.Frame and creating a Figure object with a plot. This plot is then added to the CanvasFrame using FigureCanvasWxAgg.

```python
class CanvasFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, -1, 'CanvasFrame', size=(550, 350))

        self.figure = Figure()
        self.axes = self.figure.add_subplot()
        t = np.arange(0.0, 3.0, 0.01)
        s = np.sin(2 * np.pi * t)

        self.axes.plot(t, s)
        self.canvas = FigureCanvas(self, -1, self.figure)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.EXPAND)
        self.SetSizer(self.sizer)
        self.Fit()
```

### Step 2: Add a Toolbar

To add a toolbar, a NavigationToolbar2WxAgg object is created and added to the CanvasFrame using a sizer. The update() method of the toolbar is then called to update the axes menu.

```python
    def add_toolbar(self):
        self.toolbar = NavigationToolbar(self.canvas)
        self.toolbar.Realize()
        self.sizer.Add(self.toolbar, 0, wx.LEFT | wx.EXPAND)
        self.toolbar.update()
```

### Step 3: Create the Application

The next step is to create the application by inheriting from wx.App. In the OnInit method, a CanvasFrame object is created and shown.

```python
class App(wx.App):
    def OnInit(self):
        self.Init()
        frame = CanvasFrame()
        frame.Show(True)

        return True
```

### Step 4: Run the Application

To run the application, an instance of the App object is created and the MainLoop method is called.

```python
if __name__ == "__main__":
    app = App()
    app.MainLoop()
```

## Summary

In this lab, you learned how to use Python Matplotlib to create a graph using wxagg in an application with a toolbar. You also learned how to create a CanvasFrame, add a toolbar, create an application, and run the application.
