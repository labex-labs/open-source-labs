# Data Browser Lab

## Introduction

This lab will walk you through how to interact data with multiple canvases. By selecting and highlighting a point on one axis, you will generate the data of that point on the other axis. We will be using Python Matplotlib for this lab.

## Steps

### Step 1: Import Libraries

We will start by importing the necessary libraries.

```python
import numpy as np
import matplotlib.pyplot as plt
```

### Step 2: Generate Data

We will generate random data using NumPy.

```python
np.random.seed(19680801)
X = np.random.rand(100, 200)
xs = np.mean(X, axis=1)
ys = np.std(X, axis=1)
```

### Step 3: Create Figure and Axes

We will create a figure with two axes.

```python
fig, (ax, ax2) = plt.subplots(2, 1)
```

### Step 4: Plot Data

We will plot the generated data on the first axis.

```python
line, = ax.plot(xs, ys, 'o', picker=True, pickradius=5)
```

### Step 5: Create Point Browser Class

We will create a class to handle the point browser functionality.

```python
class PointBrowser:
    def __init__(self):
        self.lastind = 0

        self.text = ax.text(0.05, 0.95, 'selected: none',
                            transform=ax.transAxes, va='top')
        self.selected, = ax.plot([xs[0]], [ys[0]], 'o', ms=12, alpha=0.4,
                                 color='yellow', visible=False)

    def on_press(self, event):
        if self.lastind is None:
            return
        if event.key not in ('n', 'p'):
            return
        if event.key == 'n':
            inc = 1
        else:
            inc = -1

        self.lastind += inc
        self.lastind = np.clip(self.lastind, 0, len(xs) - 1)
        self.update()

    def on_pick(self, event):

        if event.artist != line:
            return True

        N = len(event.ind)
        if not N:
            return True

        # the click locations
        x = event.mouseevent.xdata
        y = event.mouseevent.ydata

        distances = np.hypot(x - xs[event.ind], y - ys[event.ind])
        indmin = distances.argmin()
        dataind = event.ind[indmin]

        self.lastind = dataind
        self.update()

    def update(self):
        if self.lastind is None:
            return

        dataind = self.lastind

        ax2.clear()
        ax2.plot(X[dataind])

        ax2.text(0.05, 0.9, f'mu={xs[dataind]:1.3f}\nsigma={ys[dataind]:1.3f}',
                 transform=ax2.transAxes, va='top')
        ax2.set_ylim(-0.5, 1.5)
        self.selected.set_visible(True)
        self.selected.set_data(xs[dataind], ys[dataind])

        self.text.set_text('selected: %d' % dataind)
        fig.canvas.draw()
```

### Step 6: Connect Event Handlers

We will connect the event handlers to the figure canvas.

```python
browser = PointBrowser()

fig.canvas.mpl_connect('pick_event', browser.on_pick)
fig.canvas.mpl_connect('key_press_event', browser.on_press)
```

### Step 7: Display Plot

We will display the plot.

```python
plt.show()
```

## Summary

In this lab, we learned how to interact data with multiple canvases using Python Matplotlib. We created a class to handle the point browser functionality and connected event handlers to the figure canvas to enable interactivity.
