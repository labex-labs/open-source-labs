# Python Matplotlib Lab

## Introduction

Matplotlib is a popular data visualization library in Python. In this lab, we will learn how to embed a Matplotlib plot in a GTK4 application using the FigureCanvasGTK4Agg widget.

## Steps

### Step 1: Import the necessary libraries

```python
import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk
import numpy as np
from matplotlib.backends.backend_gtk4agg import \
    FigureCanvasGTK4Agg as FigureCanvas
from matplotlib.figure import Figure
```

We will use GTK4, numpy, and Matplotlib in this lab.

### Step 2: Define the function to create the GTK4 application window

```python
def on_activate(app):
    win = Gtk.ApplicationWindow(application=app)
    win.set_default_size(400, 300)
    win.set_title("Embedding in GTK4")
```

This function defines the GTK4 application window with a default size of 400x300 and a title of "Embedding in GTK4".

### Step 3: Create a Matplotlib figure and plot

```python
fig = Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot()
t = np.arange(0.0, 3.0, 0.01)
s = np.sin(2*np.pi*t)
ax.plot(t, s)
```

We create a Matplotlib figure with a size of 5x4 inches and a dpi of 100. We then create a subplot and plot a sine wave.

### Step 4: Create a GTK4 ScrolledWindow and set the margin

```python
sw = Gtk.ScrolledWindow(margin_top=10, margin_bottom=10,
                        margin_start=10, margin_end=10)
win.set_child(sw)
```

We create a GTK4 ScrolledWindow and set the margin to 10 pixels on each side. We then set the ScrolledWindow as the child of the application window.

### Step 5: Create a FigureCanvas and set the size request

```python
canvas = FigureCanvas(fig)
canvas.set_size_request(800, 600)
sw.set_child(canvas)
```

We create a FigureCanvas with the Matplotlib figure and set the size request to 800x600 pixels. We then set the FigureCanvas as the child of the ScrolledWindow.

### Step 6: Show the application window and run the GTK4 main loop

```python
win.show()
```

We show the application window and run the GTK4 main loop.

## Summary

In this lab, we learned how to embed a Matplotlib plot in a GTK4 application using the FigureCanvasGTK4Agg widget. We created a GTK4 application window, a Matplotlib figure, and a GTK4 ScrolledWindow with a FigureCanvas as the child. Finally, we showed the application window and ran the GTK4 main loop.
