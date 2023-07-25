# Python Matplotlib Lab

## Introduction

This lab will guide you through creating a wxPython application that displays math text in a wx.Bitmap for display in various controls on wxPython. It uses the Matplotlib library to convert text to images and the wxPython library to display the images.

## Steps

### Step 1: Install Required Libraries

To complete this lab, you need to have the following libraries installed:

- wxPython
- Matplotlib

You can install these libraries using pip.

```python
pip install wxPython
pip install matplotlib
```

### Step 2: Create a wxPython Application

Create a new Python file and import the required libraries.

```python
import wx
import numpy as np
from io import BytesIO
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
```

### Step 3: Convert Mathtext to wx.Bitmap

Define a function that converts math text to a wx.Bitmap. This function uses Matplotlib to draw the text at position (0, 0) but then relies on `facecolor="none"` and `bbox_inches="tight", pad_inches=0` to get a transparent mask that is then loaded into a wx.Bitmap.

```python
def mathtext_to_wxbitmap(s):
    fig = Figure(facecolor="none")
    text_color = (
        np.array(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT)) / 255)
    fig.text(0, 0, s, fontsize=10, color=text_color)
    buf = BytesIO()
    fig.savefig(buf, format="png", dpi=150, bbox_inches="tight", pad_inches=0)
    s = buf.getvalue()
    return wx.Bitmap.NewFromPNGData(s, len(s))
```

### Step 4: Define Functions

Define a list of functions that the application will display. Each function is defined by a math text and a lambda function that takes an input value and returns an output value.

```python
functions = [
    (r'$\sin(2 \pi x)$', lambda x: np.sin(2*np.pi*x)),
    (r'$\frac{4}{3}\pi x^3$', lambda x: (4/3)*np.pi*x**3),
    (r'$\cos(2 \pi x)$', lambda x: np.cos(2*np.pi*x)),
    (r'$\log(x)$', lambda x: np.log(x))
]
```

### Step 5: Create a Canvas Frame

Create a new class that inherits from wx.Frame. This class creates a canvas that displays the selected function.

```python
class CanvasFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, -1, title, size=(550, 350))

        self.figure = Figure()
        self.axes = self.figure.add_subplot()

        self.canvas = FigureCanvas(self, -1, self.figure)

        self.change_plot(0)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.add_buttonbar()
        self.sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)

        self.SetSizer(self.sizer)
        self.Fit()
```

### Step 6: Add a Button Bar

Add a button bar to the application that displays icons for each function. When a button is clicked, the application will display the corresponding function.

```python
    def add_buttonbar(self):
        self.button_bar = wx.Panel(self)
        self.button_bar_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer.Add(self.button_bar, 0, wx.LEFT | wx.TOP | wx.GROW)

        for i, (mt, func) in enumerate(functions):
            bm = mathtext_to_wxbitmap(mt)
            button = wx.BitmapButton(self.button_bar, 1000 + i, bm)
            self.button_bar_sizer.Add(button, 1, wx.GROW)
            self.Bind(wx.EVT_BUTTON, self.OnChangePlot, button)

        self.button_bar.SetSizer(self.button_bar_sizer)
```

### Step 7: Add a Toolbar

Add a toolbar to the application that allows the user to zoom in and out, pan, and save the plot as an image. This toolbar is added to the bottom of the frame.

```python
    def add_toolbar(self):
        self.toolbar = NavigationToolbar2Wx(self.canvas)
        self.toolbar.Realize()
        self.sizer.Add(self.toolbar, 0, wx.LEFT | wx.EXPAND)
        self.toolbar.update()
```

### Step 8: Change the Plot

Define a function that changes the plot based on the selected function. This function takes a plot_number as input and changes the plot accordingly.

```python
    def change_plot(self, plot_number):
        t = np.arange(1.0, 3.0, 0.01)
        s = functions[plot_number][1](t)
        self.axes.clear()
        self.axes.plot(t, s)
        self.canvas.draw()
```

### Step 9: Create the Application

Create a new class that inherits from wx.App. This class creates the frame and starts the event loop.

```python
class MyApp(wx.App):
    def OnInit(self):
        frame = CanvasFrame(None, "wxPython mathtext demo app")
        self.SetTopWindow(frame)
        frame.Show(True)
        return True
```

### Step 10: Run the Application

Run the application by creating an instance of the MyApp class.

```python
if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()
```

## Summary

In this lab, you learned how to create a wxPython application that displays math text in a wx.Bitmap. You used the Matplotlib library to convert text to images and the wxPython library to display the images. You also learned how to create a button bar and a toolbar in the application and how to change the plot based on the selected function.
