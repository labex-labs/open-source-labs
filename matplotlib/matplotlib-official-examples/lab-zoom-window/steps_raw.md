# Python Matplotlib Tutorial Lab

## Introduction

This lab is a step-by-step tutorial on how to connect events in one window, for example, a mouse press, to another figure window in Python Matplotlib.

## Steps

### Step 1: Set up the environment

First, we need to set up the Python environment and import the necessary libraries.

```python
import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)

figsrc, axsrc = plt.subplots(figsize=(3.7, 3.7))
figzoom, axzoom = plt.subplots(figsize=(3.7, 3.7))
axsrc.set(xlim=(0, 1), ylim=(0, 1), autoscale_on=False,
          title='Click to zoom')
axzoom.set(xlim=(0.45, 0.55), ylim=(0.4, 0.6), autoscale_on=False,
           title='Zoom window')

x, y, s, c = np.random.rand(4, 200)
s *= 200

axsrc.scatter(x, y, s, c)
axzoom.scatter(x, y, s, c)
```

### Step 2: Define the on_press function

Next, we define a function called on_press that will adjust the z and y limits of the second window based on the location of a mouse click in the first window.

```python
def on_press(event):
    if event.button != 1:
        return
    x, y = event.xdata, event.ydata
    axzoom.set_xlim(x - 0.1, x + 0.1)
    axzoom.set_ylim(y - 0.1, y + 0.1)
    figzoom.canvas.draw()
```

### Step 3: Connect the event to the function

Now, we connect the button press event in the first window to the on_press function we just defined.

```python
figsrc.canvas.mpl_connect('button_press_event', on_press)
```

### Step 4: Display the plot

Finally, we display the plot to the user.

```python
plt.show()
```

## Summary

In this lab, we learned how to connect events in one window, for example, a mouse press, to another figure window in Python Matplotlib. We also learned how to define a function to adjust the limits of the second window based on the location of a mouse click in the first window, and how to connect the button press event to this function.
