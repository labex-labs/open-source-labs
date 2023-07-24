# Matplotlib Lab: Creating a Graph with Glade 3

## Introduction

In this lab, you will learn how to create a simple graph using Matplotlib with Glade 3. Matplotlib is a plotting library for the Python programming language and can be used to create a wide variety of graphs and visualizations.

## Steps

### Step 1: Setting up the Environment

Before we start creating our graph, we need to set up the environment. Open your terminal and create a new Python file called `mpl_with_glade3.py`. Make sure you have installed the required libraries: `matplotlib`, `numpy`, `gi`, and `Gtk`.

### Step 2: Creating a Glade 3 File

Next, we will create a Glade 3 file to create the user interface for our application. Open Glade 3 and create a new project. Add a `ScrolledWindow` widget and a `Window` widget. Name the window `window1` and the scrolled window `scrolledwindow1`. Save the file as `mpl_with_glade3.glade`.

### Step 3: Creating the Graph

Now we can start creating our graph. First, import the necessary libraries and define the `Window1Signals` class. This class will handle the `destroy` signal for the window.

```python
from pathlib import Path

import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

import numpy as np

from matplotlib.backends.backend_gtk3agg import \
    FigureCanvasGTK3Agg as FigureCanvas
from matplotlib.figure import Figure


class Window1Signals:
    def on_window1_destroy(self, widget):
        Gtk.main_quit()
```

### Step 4: Defining the Main Function

Next, define the `main()` function. This function will create the user interface, create the graph, and display the window.

```python
def main():
    builder = Gtk.Builder()
    builder.add_objects_from_file(
        str(Path(__file__).parent / "mpl_with_glade3.glade"),
        ("window1", ""))
    builder.connect_signals(Window1Signals())
    window = builder.get_object("window1")
    sw = builder.get_object("scrolledwindow1")

    # Start of Matplotlib specific code
    figure = Figure(figsize=(8, 6), dpi=71)
    axis = figure.add_subplot()
    t = np.arange(0.0, 3.0, 0.01)
    s = np.sin(2*np.pi*t)
    axis.plot(t, s)

    axis.set_xlabel('time [s]')
    axis.set_ylabel('voltage [V]')

    canvas = FigureCanvas(figure)  # a Gtk.DrawingArea
    canvas.set_size_request(800, 600)
    sw.add(canvas)
    # End of Matplotlib specific code

    window.show_all()
    Gtk.main()

if __name__ == "__main__":
    main()
```

### Step 5: Running the Application

Save the file and run it using the terminal command `python mpl_with_glade3.py`. The window with the graph should appear.

## Summary

Congratulations! You have successfully created a graph using Matplotlib with Glade 3. You can use this as a starting point to create more complex graphs and visualizations.
