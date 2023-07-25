# Python Matplotlib Tutorial Lab

## Introduction

In this lab, we will learn how to use `pyplot` to manage figure windows, but modify the GUI by accessing the underlying GTK widgets. We will create a figure with two plots and add a button to the toolbar and a label to the canvas. We will also add functionality to display the coordinates of the cursor when it moves over the plots.

## Steps

### Step 1: Import the required libraries

```python
import matplotlib
matplotlib.use('GTK4Agg')
import gi
import matplotlib.pyplot as plt

gi.require_version('Gtk', '4.0')
from gi.repository import Gtk
```

We import the required libraries including `matplotlib`, `gi`, `pyplot`, and `Gtk`. We set the backend of matplotlib to use GTK4.

### Step 2: Create the figure and plots

```python
fig, ax = plt.subplots()
ax.plot([1, 2, 3], 'ro-', label='easy as 1 2 3')
ax.plot([1, 4, 9], 'gs--', label='easy as 1 2 3 squared')
ax.legend()
```

We create a figure with two subplots and plot two sets of data on them. We also add a legend to the plots.

### Step 3: Access the toolbar and vbox

```python
manager = fig.canvas.manager
toolbar = manager.toolbar
vbox = manager.vbox
```

We access the `toolbar` and `vbox` attributes of the figure canvas manager.

### Step 4: Add a button to the toolbar

```python
button = Gtk.Button(label='Click me')
button.connect('clicked', lambda button: print('hi mom'))
button.set_tooltip_text('Click me for fun and profit')
toolbar.append(button)
```

We create a button with a label and a tooltip, and connect it to a function that prints a message to the console. We add the button to the toolbar.

### Step 5: Add a label to the canvas

```python
label = Gtk.Label()
label.set_markup('Drag mouse over axes for position')
vbox.insert_child_after(label, fig.canvas)
```

We create a label and set its text. We add the label to the vbox after the figure canvas.

### Step 6: Update the label with cursor coordinates

```python
def update(event):
    if event.xdata is None:
        label.set_markup('Drag mouse over axes for position')
    else:
        label.set_markup(
            f'<span color="#ef0000">x,y=({event.xdata}, {event.ydata})</span>')

fig.canvas.mpl_connect('motion_notify_event', update)
```

We create a function that updates the label with the x and y coordinates of the cursor when it moves over the plots. We connect the function to the `motion_notify_event` of the canvas.

### Step 7: Display the figure

```python
plt.show()
```

We display the figure with the added button and label.

## Summary

In this lab, we learned how to use `pyplot` to manage figure windows, but modify the GUI by accessing the underlying GTK widgets. We created a figure with two plots, added a button to the toolbar, and a label to the canvas. We also added functionality to display the coordinates of the cursor when it moves over the plots. This lab provides a basic understanding of how to customize the GUI of a matplotlib figure using GTK4.
