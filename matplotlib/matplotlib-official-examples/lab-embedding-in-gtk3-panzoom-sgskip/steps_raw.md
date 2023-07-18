# Matplotlib Embedding in GTK3 Lab

## Introduction

This lab will guide you through the steps to embed a Matplotlib plot with navigation toolbar in a GTK3 window using PyGObject. GTK3 is a cross-platform widget toolkit for creating graphical user interfaces. Matplotlib is a plotting library for creating static, animated, and interactive visualizations in Python.

## Steps

### Step 1: Import Required Libraries

First, we need to import the required libraries. We will be using `gi` library to access GTK3 widgets, and Matplotlib's `FigureCanvas` and `NavigationToolbar` for embedding a plot with navigation toolbar.

```python
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import numpy as np
from matplotlib.backends.backend_gtk3 import NavigationToolbar2GTK3 as NavigationToolbar
from matplotlib.backends.backend_gtk3agg import FigureCanvasGTK3Agg as FigureCanvas
from matplotlib.figure import Figure
```

### Step 2: Create a GTK3 Window

Next, we will create a GTK3 window with a title, default size, and connect the "delete-event" signal to `Gtk.main_quit` function to close the window when the close button is clicked.

```python
win = Gtk.Window()
win.connect("delete-event", Gtk.main_quit)
win.set_default_size(400, 300)
win.set_title("Embedding in GTK3")
```

### Step 3: Create a Matplotlib Figure and Plot Data

Now, we will create a Matplotlib figure with a subplot and plot data on it.

```python
fig = Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(1, 1, 1)
t = np.arange(0.0, 3.0, 0.01)
s = np.sin(2*np.pi*t)
ax.plot(t, s)
```

### Step 4: Add Figure Canvas and Navigation Toolbar to GTK3 Window

Next, we will add a Matplotlib figure canvas to the GTK3 window using a `Gtk.VBox` container. We will also add a navigation toolbar to the window using `NavigationToolbar` and pack it into the same `Gtk.VBox` container.

```python
vbox = Gtk.VBox()
win.add(vbox)

# Add canvas to vbox
canvas = FigureCanvas(fig)  # a Gtk.DrawingArea
vbox.pack_start(canvas, True, True, 0)

# Create toolbar
toolbar = NavigationToolbar(canvas)
vbox.pack_start(toolbar, False, False, 0)
```

### Step 5: Show the GTK3 Window

Finally, we will show all the widgets in the window and start the GTK3 main loop.

```python
win.show_all()
Gtk.main()
```

## Summary

Congratulations! You have successfully embedded a Matplotlib plot with navigation toolbar in a GTK3 window using PyGObject. This can be useful when creating GUI applications that require data visualization.
