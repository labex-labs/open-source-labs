# Matplotlib Figure and Axes Enter/Leave Events Lab

## Introduction

Matplotlib is a data visualization library for Python. It offers a variety of tools for creating static, animated, and interactive visualizations in Python. One of the interactive features of Matplotlib is the ability to detect when the mouse enters and leaves a figure or an axes. In this lab, we will learn how to use Matplotlib's Figure and Axes enter/leave events to change the frame colors of the figure and axes.

## Steps

### Step 1: Importing Matplotlib

Before we start using Matplotlib, we need to import it. We will also import the pyplot module, which provides a simple interface for creating plots.

```python
import matplotlib.pyplot as plt
```

### Step 2: Creating the Figure and Axes

We will create a figure with two subplots (axes) using the `subplots` function. We will also set the title of the figure.

```python
fig, axs = plt.subplots(2, 1)
fig.suptitle('Mouse Hover Over Figure or Axes to Trigger Events')
```

### Step 3: Defining the Event Handlers

We will now define four event handler functions: `on_enter_axes`, `on_leave_axes`, `on_enter_figure`, and `on_leave_figure`. These functions will be called when the mouse enters or leaves an axes or the figure.

```python
def on_enter_axes(event):
    print('enter_axes', event.inaxes)
    event.inaxes.patch.set_facecolor('yellow')
    event.canvas.draw()

def on_leave_axes(event):
    print('leave_axes', event.inaxes)
    event.inaxes.patch.set_facecolor('white')
    event.canvas.draw()

def on_enter_figure(event):
    print('enter_figure', event.canvas.figure)
    event.canvas.figure.patch.set_facecolor('red')
    event.canvas.draw()

def on_leave_figure(event):
    print('leave_figure', event.canvas.figure)
    event.canvas.figure.patch.set_facecolor('grey')
    event.canvas.draw()
```

### Step 4: Connecting the Event Handlers to the Figure Canvas

We will now connect the event handlers to the figure canvas using the `mpl_connect` method. This will allow the event handlers to be triggered when the mouse enters or leaves the figure or axes.

```python
fig.canvas.mpl_connect('figure_enter_event', on_enter_figure)
fig.canvas.mpl_connect('figure_leave_event', on_leave_figure)
fig.canvas.mpl_connect('axes_enter_event', on_enter_axes)
fig.canvas.mpl_connect('axes_leave_event', on_leave_axes)
```

### Step 5: Displaying the Figure

We will now display the figure using the `show` function.

```python
plt.show()
```

## Summary

In this lab, we learned how to use Matplotlib's Figure and Axes enter/leave events to change the frame colors of the figure and axes. We created a figure with two subplots, defined event handler functions for entering and leaving the figure and axes, connected the event handlers to the figure canvas, and displayed the figure.
