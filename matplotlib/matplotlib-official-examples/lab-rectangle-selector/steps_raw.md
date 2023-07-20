# Python Matplotlib Tutorial

## Introduction

In this lab, we will learn how to use the RectangleSelector and EllipseSelector widgets in Matplotlib to draw a rectangle or ellipse from the initial click position to the current mouse position.

## Steps

### Step 1: Import necessary libraries

We will start by importing the necessary libraries: Matplotlib, Numpy, and the RectangleSelector and EllipseSelector widgets.

```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import EllipseSelector, RectangleSelector
```

### Step 2: Define the select callback function

The select callback function will be called every time the user selects a rectangle or ellipse. The function will receive the click and release events as arguments and print out the coordinates of the rectangle or ellipse.

```python
def select_callback(eclick, erelease):
    """
    Callback for line selection.

    *eclick* and *erelease* are the press and release events.
    """
    x1, y1 = eclick.xdata, eclick.ydata
    x2, y2 = erelease.xdata, erelease.ydata
    print(f"({x1:3.2f}, {y1:3.2f}) --> ({x2:3.2f}, {y2:3.2f})")
    print(f"The buttons you used were: {eclick.button} {erelease.button}")
```

### Step 3: Define the toggle selector function

The toggle selector function will be called every time the user presses the 't' key. This function will toggle the active status of the RectangleSelector and EllipseSelector widgets.

```python
def toggle_selector(event):
    print('Key pressed.')
    if event.key == 't':
        for selector in selectors:
            name = type(selector).__name__
            if selector.active:
                print(f'{name} deactivated.')
                selector.set_active(False)
            else:
                print(f'{name} activated.')
                selector.set_active(True)
```

### Step 4: Create the figure and subplots

We will create a figure with two subplots, one for the RectangleSelector and one for the EllipseSelector.

```python
fig = plt.figure(layout='constrained')
axs = fig.subplots(2)
```

### Step 5: Plot something on the subplots

We will plot something on the subplots, so that the user can see the effect of the RectangleSelector and EllipseSelector.

```python
N = 100000  # If N is large one can see improvement by using blitting.
x = np.linspace(0, 10, N)

for ax in axs:
    ax.plot(x, np.sin(2*np.pi*x))  # plot something
```

### Step 6: Create the RectangleSelector and EllipseSelector widgets

We will create the RectangleSelector and EllipseSelector widgets and add them to the subplots.

```python
selectors = []
for ax, selector_class in zip(axs, [RectangleSelector, EllipseSelector]):
    ax.set_title(f"Click and drag to draw a {selector_class.__name__}.")
    selectors.append(selector_class(
        ax, select_callback,
        useblit=True,
        button=[1, 3],  # disable middle button
        minspanx=5, minspany=5,
        spancoords='pixels',
        interactive=True))
    fig.canvas.mpl_connect('key_press_event', toggle_selector)
axs[0].set_title("Press 't' to toggle the selectors on and off.\n"
                 + axs[0].get_title())
```

### Step 7: Show the plot

Finally, we will show the plot to the user.

```python
plt.show()
```

## Summary

In this lab, we learned how to use the RectangleSelector and EllipseSelector widgets in Matplotlib to draw a rectangle or ellipse from the initial click position to the current mouse position. We also learned how to create a figure with subplots, plot something on the subplots, and toggle the active status of the widgets using a key press event.
