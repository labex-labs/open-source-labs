# Embedding Matplotlib in GTK4

## Introduction

This lab will guide you through the process of embedding Matplotlib in GTK4, using Python. Matplotlib is a data visualization library that allows users to create a wide range of static, animated, and interactive visualizations in Python. GTK4 is a toolkit for creating graphical user interfaces (GUIs) in Python.

## Steps

### Step 1: Install Dependencies

Before we begin, make sure you have the necessary dependencies installed. In addition to Python 3, you will need to install the GTK4 and Matplotlib libraries. If you're using a virtual environment, activate it before installing the libraries.

```
pip install pygobject
pip install matplotlib
```

### Step 2: Import Libraries

Import the necessary libraries for this lab: GTK4, Matplotlib, and NumPy.

```python
import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk
import numpy as np
from matplotlib.backends.backend_gtk4 import NavigationToolbar2GTK4 as NavigationToolbar
from matplotlib.backends.backend_gtk4agg import FigureCanvasGTK4Agg as FigureCanvas
from matplotlib.figure import Figure
```

### Step 3: Create the Application

Create a GTK4 application and specify the window size and title.

```python
def on_activate(app):
    win = Gtk.ApplicationWindow(application=app)
    win.set_default_size(400, 300)
    win.set_title("Embedding in GTK4")
```

### Step 4: Create the Figure

Create a Figure object and add a subplot to it. In this example, we're creating a sine wave plot.

```python
fig = Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(1, 1, 1)
t = np.arange(0.0, 3.0, 0.01)
s = np.sin(2*np.pi*t)
ax.plot(t, s)
```

### Step 5: Add the Canvas

Add a canvas to the GTK4 window. The canvas is a Gtk.DrawingArea that contains the Matplotlib Figure.

```python
vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
win.set_child(vbox)

canvas = FigureCanvas(fig)
canvas.set_hexpand(True)
canvas.set_vexpand(True)
vbox.append(canvas)
```

### Step 6: Add the Navigation Toolbar

Add a navigation toolbar to the GTK4 window. The toolbar allows the user to pan and zoom the plot, save the plot as an image, and more.

```python
toolbar = NavigationToolbar(canvas)
vbox.append(toolbar)
```

### Step 7: Show the Window

Display the GTK4 window.

```python
win.show()
```

### Summary

In this lab, you learned how to embed Matplotlib in a GTK4 window using Python. The steps included installing the necessary dependencies, importing the required libraries, creating a GTK4 application, creating a Matplotlib Figure, adding a canvas to the GTK4 window, adding a navigation toolbar to the GTK4 window, and displaying the GTK4 window. You should now be able to create your own Matplotlib plots in GTK4 windows.
