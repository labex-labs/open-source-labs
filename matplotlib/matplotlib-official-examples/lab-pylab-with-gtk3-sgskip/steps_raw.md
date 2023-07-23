# Python Matplotlib Tutorial

## Introduction

In this lab, we will learn how to use the Matplotlib library to create and modify figure windows. We will also explore how to customize the GUI by accessing the underlying GTK widgets.

## Steps

### Step 1: Import Libraries

First, we need to import the necessary libraries. We will be using Matplotlib, GTK3, and the Gtk module from the gi.repository.

```python
import matplotlib
matplotlib.use('GTK3Agg')  # or 'GTK3Cairo'
import gi
import matplotlib.pyplot as plt
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
```

### Step 2: Create Figure and Axis

Next, we will create a figure and axis using the `subplots()` method. We will then plot two lines on the axis and add a legend to distinguish them.

```python
fig, ax = plt.subplots()
ax.plot([1, 2, 3], 'ro-', label='easy as 1 2 3')
ax.plot([1, 4, 9], 'gs--', label='easy as 1 2 3 squared')
ax.legend()
```

### Step 3: Access Toolbar and VBox

We will access the toolbar and vbox attributes of the figure canvas manager using the `manager.toolbar` and `manager.vbox` methods, respectively.

```python
manager = fig.canvas.manager
toolbar = manager.toolbar
vbox = manager.vbox
```

### Step 4: Add Button to Toolbar

We will add a button to the toolbar using the Gtk module. First, we create a button with a label and connect it to a function to print a message when clicked. Then, we create a toolitem, set its tooltip text, add the button to it, and insert it into the toolbar.

```python
button = Gtk.Button(label='Click me')
button.show()
button.connect('clicked', lambda button: print('hi mom'))

toolitem = Gtk.ToolItem()
toolitem.show()
toolitem.set_tooltip_text('Click me for fun and profit')
toolitem.add(button)

pos = 8  # where to insert this in the toolbar
toolbar.insert(toolitem, pos)
```

### Step 5: Add Label to VBox

We will add a label to the vbox to display the x,y coordinates of the mouse when it is dragged over the axis. First, we create a label with some text and add it to the vbox.

```python
label = Gtk.Label()
label.set_markup('Drag mouse over axes for position')
label.show()
vbox.pack_start(label, False, False, 0)
```

### Step 6: Update Label Text on Mouse Movement

We will update the label text to display the x,y coordinates of the mouse when it is dragged over the axis. We create a function to update the label text and connect it to the `motion_notify_event` using the `mpl_connect()` method.

```python
def update(event):
    if event.xdata is None:
        label.set_markup('Drag mouse over axes for position')
    else:
        label.set_markup(
            f'<span color="#ef0000">x,y=({event.xdata}, {event.ydata})</span>')

fig.canvas.mpl_connect('motion_notify_event', update)
```

### Step 7: Display the Plot

Finally, we display the plot using the `show()` method.

```python
plt.show()
```

## Summary

In this lab, we learned how to use Matplotlib to create and modify figure windows. We also explored how to customize the GUI by accessing the underlying GTK widgets. We added a button to the toolbar and a label to the vbox, and updated the label text on mouse movement. We also plotted two lines on an axis and added a legend to distinguish them.
