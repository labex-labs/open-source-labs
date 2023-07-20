# Matplotlib Tutorial Lab

## Introduction

In this lab, you will learn how to embed Matplotlib in a Gtk4 application and interact with a treeview to store data. You will be able to plot data by double-clicking on an entry in the treeview.

## Steps

### Step 1: Set up the Environment

First, you need to create a virtual environment and install the necessary packages.

```bash
# create virtual environment
python3 -m venv matplotlib_tutorial

# activate the environment
source matplotlib_tutorial/bin/activate

# install necessary packages
pip install numpy matplotlib PyGObject
```

### Step 2: Create the Application Window

Next, you need to create the application window that will contain the treeview and the Matplotlib plot.

```python
import gi

gi.require_version('Gtk', '4.0')
from gi.repository import Gtk

from numpy.random import random

from matplotlib.backends.backend_gtk4agg import FigureCanvas
from matplotlib.figure import Figure


class DataManager(Gtk.ApplicationWindow):
    num_rows, num_cols = 20, 10

    data = random((num_rows, num_cols))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_default_size(600, 600)

        self.set_title('GtkListStore demo')

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, homogeneous=False,
                       spacing=8)
        self.set_child(vbox)

        label = Gtk.Label(label='Double click a row to plot the data')
        vbox.append(label)

        sw = Gtk.ScrolledWindow()
        sw.set_has_frame(True)
        sw.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        sw.set_hexpand(True)
        sw.set_vexpand(True)
        vbox.append(sw)

        model = self.create_model()
        self.treeview = Gtk.TreeView(model=model)
        self.treeview.connect('row-activated', self.plot_row)
        sw.set_child(self.treeview)

        fig = Figure(figsize=(6, 4), layout='constrained')

        self.canvas = FigureCanvas(fig)
        self.canvas.set_hexpand(True)
        self.canvas.set_vexpand(True)
        vbox.append(self.canvas)
        ax = fig.add_subplot()
        self.line, = ax.plot(self.data[0, :], 'go')

        self.add_columns()

    def plot_row(self, treeview, path, view_column):
        ind, = path
        points = self.data[ind, :]
        self.line.set_ydata(points)
        self.canvas.draw()

    def add_columns(self):
        for i in range(self.num_cols):
            column = Gtk.TreeViewColumn(str(i), Gtk.CellRendererText(), text=i)
            self.treeview.append_column(column)

    def create_model(self):
        types = [float] * self.num_cols
        store = Gtk.ListStore(*types)
        for row in self.data:
            it = store.insert(-1)
            store.set(it, {i: val for i, val in enumerate(row)})
        return store


def on_activate(app):
    manager = DataManager(application=app)
    manager.show()


app = Gtk.Application(application_id='org.matplotlib.examples.GTK4Spreadsheet')
app.connect('activate', on_activate)
app.run()
```

### Step 3: Plot the Data

Now, you will plot the data by double-clicking on an entry in the treeview.

```python
    def plot_row(self, treeview, path, view_column):
        ind, = path
        points = self.data[ind, :]
        self.line.set_ydata(points)
        self.canvas.draw()
```

### Step 4: Add Columns to the Treeview

You need to add columns to the treeview to display the data.

```python
    def add_columns(self):
        for i in range(self.num_cols):
            column = Gtk.TreeViewColumn(str(i), Gtk.CellRendererText(), text=i)
            self.treeview.append_column(column)
```

### Step 5: Create the Model

Finally, you need to create the model to store the data.

```python
    def create_model(self):
        types = [float] * self.num_cols
        store = Gtk.ListStore(*types)
        for row in self.data:
            it = store.insert(-1)
            store.set(it, {i: val for i, val in enumerate(row)})
        return store
```

## Summary

In this lab, you learned how to embed Matplotlib in a Gtk4 application and interact with a treeview to store data. You can now plot data by double-clicking on an entry in the treeview.
