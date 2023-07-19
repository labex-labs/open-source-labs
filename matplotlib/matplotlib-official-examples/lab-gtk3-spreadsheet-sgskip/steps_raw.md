# Matplotlib Lab

## Introduction

Matplotlib is a popular Python library for creating static, animated, and interactive visualizations in Python. In this lab, you will learn how to embed Matplotlib in a GTK3 application and interact with a treeview to store data.

## Steps

### Step 1: Set up the Environment

Before getting started, we need to set up our environment. We'll start by creating a new Python file and importing the necessary libraries.

```python
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
from gi.repository import Gdk, Gtk
from numpy.random import random
from matplotlib.backends.backend_gtk3agg import FigureCanvas
from matplotlib.figure import Figure
```

### Step 2: Create the Data Manager Window

In this step, we'll create the `DataManager` class that extends from the `Gtk.Window` class. This class will be responsible for managing the data that we want to plot.

```python
class DataManager(Gtk.Window):
    num_rows, num_cols = 20, 10
    data = random((num_rows, num_cols))
```

### Step 3: Set Up the Window

In this step, we'll set up the window that will display our data. We'll start by initializing the window with a title and a size.

```python
def __init__(self):
    super().__init__()
    self.set_default_size(600, 600)
    self.connect('destroy', lambda win: Gtk.main_quit())
    self.set_title('GtkListStore demo')
    self.set_border_width(8)
```

### Step 4: Add a Label

In this step, we'll add a label to the window that will prompt the user to double-click a row to plot the data.

```python
vbox = Gtk.VBox(homogeneous=False, spacing=8)
self.add(vbox)
label = Gtk.Label(label='Double click a row to plot the data')
vbox.pack_start(label, False, False, 0)
```

### Step 5: Add a TreeView

In this step, we'll add a treeview to the window that will display our data. We'll also create a model to store the data.

```python
sw = Gtk.ScrolledWindow()
sw.set_shadow_type(Gtk.ShadowType.ETCHED_IN)
sw.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
vbox.pack_start(sw, True, True, 0)
model = self.create_model()
self.treeview = Gtk.TreeView(model=model)
self.treeview.connect('row-activated', self.plot_row)
sw.add(self.treeview)
self.add_columns()
```

### Step 6: Create the Matplotlib Plot

In this step, we'll create a Matplotlib plot that will display our data. We'll start by creating a figure and adding a subplot.

```python
fig = Figure(figsize=(6, 4))
self.canvas = FigureCanvas(fig)
vbox.pack_start(self.canvas, True, True, 0)
ax = fig.add_subplot()
```

### Step 7: Plot the Data

In this step, we'll plot the first row of our data on the Matplotlib plot.

```python
self.line, = ax.plot(self.data[0, :], 'go')
```

### Step 8: Implement Plotting Functionality

In this step, we'll implement the functionality to plot the data when a row is double-clicked.

```python
def plot_row(self, treeview, path, view_column):
    ind, = path
    points = self.data[ind, :]
    self.line.set_ydata(points)
    self.canvas.draw()
```

### Step 9: Add Columns to TreeView

In this step, we'll add columns to the treeview that will display our data.

```python
def add_columns(self):
    for i in range(self.num_cols):
        column = Gtk.TreeViewColumn(str(i), Gtk.CellRendererText(), text=i)
        self.treeview.append_column(column)
```

### Step 10: Create the Model

In this step, we'll create the model that will store our data.

```python
def create_model(self):
    types = [float] * self.num_cols
    store = Gtk.ListStore(*types)
    for row in self.data:
        store.append(tuple(row))
    return store
```

### Step 11: Show the Window

In this step, we'll show the window that displays our data.

```python
manager = DataManager()
manager.show_all()
Gtk.main()
```

## Summary

In this lab, you learned how to embed Matplotlib in a GTK3 application and interact with a treeview to store data. You also learned how to plot data using Matplotlib and how to create a model to store data in a treeview.
