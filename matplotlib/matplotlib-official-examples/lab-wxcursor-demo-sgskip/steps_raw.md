# Adding a Cursor in WX Tutorial

## Introduction

This tutorial will guide you through the process of adding a cursor in WX to report data coordinates. We will be using Matplotlib, a plotting library for Python that provides tools to create a variety of plots, charts, and graphs.

## Steps

### Step 1: Create a Canvas Frame

First, we will create a canvas frame that will hold the Matplotlib plot. We will add a sinusoidal plot to demonstrate the cursor functionality.

```python
class CanvasFrame(wx.Frame):
    def __init__(self, ):
        super().__init__(None, -1, 'CanvasFrame', size=(550, 350))

        # Create a Figure and add a subplot
        self.figure = Figure()
        self.axes = self.figure.add_subplot()
        t = np.arange(0.0, 3.0, 0.01)
        s = np.sin(2*np.pi*t)

        # Plot the sinusoidal curve
        self.axes.plot(t, s)
        self.axes.set_xlabel('t')
        self.axes.set_ylabel('sin(t)')

        # Create a FigureCanvas to display the plot
        self.figure_canvas = FigureCanvas(self, -1, self.figure)

        # Bind the motion_notify_event to update the status bar
        self.figure_canvas.mpl_connect(
            'motion_notify_event', self.UpdateStatusBar)

        # Bind the enter_window event to change the cursor
        self.figure_canvas.Bind(wx.EVT_ENTER_WINDOW, self.ChangeCursor)

        # Create a sizer and add the FigureCanvas to it
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.figure_canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
        self.SetSizer(self.sizer)
        self.Fit()

        # Create a status bar to report the cursor location
        self.statusBar = wx.StatusBar(self, -1)
        self.SetStatusBar(self.statusBar)

        # Create a toolbar to navigate the plot
        self.toolbar = NavigationToolbar2Wx(self.figure_canvas)
        self.sizer.Add(self.toolbar, 0, wx.LEFT | wx.EXPAND)
        self.toolbar.Show()
```

### Step 2: Change the Cursor

Next, we will define a method to change the cursor when it enters the canvas frame. In this case, we will change the cursor to a bullseye.

```python
def ChangeCursor(self, event):
    self.figure_canvas.SetCursor(wx.Cursor(wx.CURSOR_BULLSEYE))
```

### Step 3: Update the Status Bar

Finally, we will define a method to update the status bar with the cursor location whenever the mouse moves over the plot.

```python
def UpdateStatusBar(self, event):
    if event.inaxes:
        self.statusBar.SetStatusText(f"x={event.xdata}  y={event.ydata}")
```

### Summary

Congratulations! You have successfully added a cursor in WX to report data coordinates using Matplotlib. By following the steps outlined in this tutorial, you can easily customize the cursor to fit your needs.
