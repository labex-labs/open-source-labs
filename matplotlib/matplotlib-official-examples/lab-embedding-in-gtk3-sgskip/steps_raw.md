# **Lab: Embedding Matplotlib in GTK3**

## Introduction

In this lab, you will learn how to embed a Matplotlib figure into a GTK3 application using the `FigureCanvasGTK3Agg` widget. GTK, or GIMP Toolkit, is a popular widget toolkit for creating graphical user interfaces (GUIs) in Linux and other Unix-like operating systems.

## Steps

### Step 1: Install Dependencies

Before you begin, make sure you have the necessary dependencies installed. You will need Python, GTK3, and Matplotlib. You can install these using the following commands:

```bash
sudo apt-get update
sudo apt-get install python3 python3-gi python3-gi-cairo gir1.2-gtk-3.0 python3-matplotlib
```

### Step 2: Create a GTK3 Window

The first step is to create a GTK3 window using the `Gtk.Window` class. We will also set the window's size and title, and connect the `delete-event` signal to the `Gtk.main_quit` function so that the window can be closed.

```python
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

win = Gtk.Window()
win.connect("delete-event", Gtk.main_quit)
win.set_default_size(400, 300)
win.set_title("Embedding in GTK3")
```

### Step 3: Create a Matplotlib Figure

Next, we will create a Matplotlib figure using the `Figure` class. We will also add a subplot to the figure, plot a sine wave using NumPy, and label the axes.

```python
import numpy as np
from matplotlib.figure import Figure

fig = Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot()
t = np.arange(0.0, 3.0, 0.01)
s = np.sin(2*np.pi*t)
ax.plot(t, s)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Amplitude')
ax.set_title('Sine Wave')
```

### Step 4: Create a Scrolled Window

In order to display the Matplotlib figure, we will need to create a `Gtk.ScrolledWindow` widget. This will allow us to scroll through the figure if it is too large to fit in the window. We will also set the border width and add the scrolled window to the GTK3 window.

```python
sw = Gtk.ScrolledWindow()
win.add(sw)
sw.set_border_width(10)
```

### Step 5: Add the Figure to the Scrolled Window

Now we can create a `FigureCanvasGTK3Agg` widget and add it to the scrolled window. This widget will display the Matplotlib figure.

```python
from matplotlib.backends.backend_gtk3agg import FigureCanvasGTK3Agg as FigureCanvas

canvas = FigureCanvas(fig)
canvas.set_size_request(800, 600)
sw.add(canvas)
```

### Step 6: Show the Window

Finally, we can show the GTK3 window and start the main loop.

```python
win.show_all()
Gtk.main()
```

## Summary

In this lab, you learned how to embed a Matplotlib figure into a GTK3 application using the `FigureCanvasGTK3Agg` widget. You also learned how to create a GTK3 window and a scrolled window, and how to display a sine wave using Matplotlib and NumPy.
