# Lab: Creating a Looking Glass with Matplotlib

## Introduction

This lab will guide you through creating a looking glass effect using mouse events in Matplotlib. This example will allow you to inspect data in a circular area that can be moved around by clicking and dragging.

## Steps

### Step 1: Importing the Required Libraries

We need to import the Matplotlib library, NumPy library and the Matplotlib patches module. We will use these libraries to create our looking glass effect.

```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches
```

### Step 2: Generating the Random Data

We will generate two sets of random data using NumPy. This data will be plotted to create a scatterplot.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

x, y = np.random.rand(2, 200)
```

### Step 3: Creating the Figure and Axes

We will create the figure and axes object using the `subplots()` function. We will also add a yellow circle patch to the axes object using the `patches.Circle()` function.

```python
fig, ax = plt.subplots()
circ = patches.Circle((0.5, 0.5), 0.25, alpha=0.8, fc='yellow')
ax.add_patch(circ)
```

### Step 4: Plotting the Data

We will plot the random data generated in Step 2 using the `plot()` function twice. The first plot will have an alpha value of 0.2 and the second plot will have an alpha value of 1.0 and a clip path set to the yellow circle patch.

```python
ax.plot(x, y, alpha=0.2)
line, = ax.plot(x, y, alpha=1.0, clip_path=circ)
ax.set_title("Left click and drag to move looking glass")
```

### Step 5: Creating the Event Handler

We will create an event handler class that will handle the mouse events needed to move the yellow circle patch around the plot. This class will contain three methods: `on_press()`, `on_release()`, and `on_move()`.

```python
class EventHandler:
    def __init__(self):
        fig.canvas.mpl_connect('button_press_event', self.on_press)
        fig.canvas.mpl_connect('button_release_event', self.on_release)
        fig.canvas.mpl_connect('motion_notify_event', self.on_move)
        self.x0, self.y0 = circ.center
        self.pressevent = None

    def on_press(self, event):
        if event.inaxes != ax:
            return

        if not circ.contains(event)[0]:
            return

        self.pressevent = event

    def on_release(self, event):
        self.pressevent = None
        self.x0, self.y0 = circ.center

    def on_move(self, event):
        if self.pressevent is None or event.inaxes != self.pressevent.inaxes:
            return

        dx = event.xdata - self.pressevent.xdata
        dy = event.ydata - self.pressevent.ydata
        circ.center = self.x0 + dx, self.y0 + dy
        line.set_clip_path(circ)
        fig.canvas.draw()

handler = EventHandler()
plt.show()
```

### Step 6: Running the Program

Run the program and left-click and drag the yellow circle patch to move it around the plot. You can use this effect to inspect data within the circular area.

## Summary

In this lab, we learned how to create a looking glass effect using mouse events in Matplotlib. We generated random data, plotted the data, and created an event handler class to handle mouse events. By left-clicking and dragging the yellow circle patch, we were able to move it around the plot and inspect data within the circular area.
