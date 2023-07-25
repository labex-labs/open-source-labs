# Mouse Interaction with Matplotlib Plot

## Introduction

This lab demonstrates an example of how to interact with the plotting canvas by connecting to move and click events using Matplotlib library in Python. Matplotlib is a data visualization library that allows users to create static, animated, and interactive visualizations in Python.

## Steps

### Step 1: Creating a Sine Wave Plot

First, we need to create a sine wave plot using numpy and matplotlib libraries.

```python
import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0, 1.0, 0.01)
s = np.sin(2 * np.pi * t)
fig, ax = plt.subplots()
ax.plot(t, s)
```

### Step 2: Mouse Move Event

We can connect to mouse move events using the `motion_notify_event` method. In this example, we are printing the x and y data coordinates and x and y pixel coordinates when the mouse moves over the plot.

```python
def on_move(event):
    if event.inaxes:
        print(f'data coords {event.xdata} {event.ydata},',
              f'pixel coords {event.x} {event.y}')

binding_id = plt.connect('motion_notify_event', on_move)
```

### Step 3: Mouse Click Event

We can connect to mouse click events using the `button_press_event` method. In this example, we are disconnecting the mouse move event callback when the left mouse button is clicked.

```python
from matplotlib.backend_bases import MouseButton

def on_click(event):
    if event.button is MouseButton.LEFT:
        print('disconnecting callback')
        plt.disconnect(binding_id)

plt.connect('button_press_event', on_click)
```

### Step 4: Displaying the Plot

Finally, we need to display the plot using the `show` method.

```python
plt.show()
```

## Summary

This lab demonstrated how to interact with a Matplotlib plot using mouse move and click events. By connecting to these events, we can perform various actions like printing the coordinates of the mouse pointer, disconnecting callbacks, etc. This technique can be useful to create interactive visualizations in Python.
