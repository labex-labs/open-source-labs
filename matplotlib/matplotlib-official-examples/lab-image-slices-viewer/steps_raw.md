# Matplotlib Scroll Event Lab

## Introduction

This lab will guide you through a step-by-step process of how to use the scroll event in Matplotlib. The scroll event can be used to navigate through 2D slices of 3D data.

## Steps

### Step 1: Import necessary libraries

First, we need to import the necessary libraries which include Matplotlib and NumPy.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Create the data

We will create 3D data using NumPy's `ogrid` function.

```python
x, y, z = np.ogrid[-10:10:100j, -10:10:100j, 1:10:20j]
X = np.sin(x * y * z) / (x * y * z)
```

### Step 3: Create the IndexTracker class

The `IndexTracker` class will keep track of the current slice index and update the plot accordingly.

```python
class IndexTracker:
    def __init__(self, ax, X):
        self.index = 0
        self.X = X
        self.ax = ax
        self.im = ax.imshow(self.X[:, :, self.index])
        self.update()

    def on_scroll(self, event):
        increment = 1 if event.button == 'up' else -1
        max_index = self.X.shape[-1] - 1
        self.index = np.clip(self.index + increment, 0, max_index)
        self.update()

    def update(self):
        self.im.set_data(self.X[:, :, self.index])
        self.ax.set_title(
            f'Use scroll wheel to navigate\nindex {self.index}')
        self.im.axes.figure.canvas.draw()
```

### Step 4: Create the plot and connect the scroll event

We will create the plot using Matplotlib's `subplots` function and pass the created `IndexTracker` object to it. Then, we will connect the scroll event to the figure canvas using `mpl_connect`.

```python
fig, ax = plt.subplots()
tracker = IndexTracker(ax, X)

fig.canvas.mpl_connect('scroll_event', tracker.on_scroll)
plt.show()
```

## Summary

In this lab, we learned how to use the scroll event in Matplotlib to navigate through 2D slices of 3D data. We created a `IndexTracker` class to keep track of the current slice index and updated the plot accordingly. Finally, we created the plot and connected the scroll event to the figure canvas.
