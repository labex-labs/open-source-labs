# Matplotlib Lasso Demo

## Introduction

In this lab, you will learn how to use the Matplotlib library to create an interactive plot that allows users to select a set of points using a lasso tool. You will also learn how to use a callback function to change the color of the selected points.

## Steps

### Step 1: Import Libraries

First, import the necessary libraries for the lab. We will be using `matplotlib` to create the plot and `numpy` to generate random data.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Create the Lasso Manager Class

Next, create the `LassoManager` class that will handle the lasso functionality. The `__init__` method initializes the plot and collection object. The `callback` method changes the color of the selected points, and the `on_press` and `on_release` methods handle the mouse events.

```python
class LassoManager:
    def __init__(self, ax, data):
        # The information of whether a point has been selected or not is stored in the
        # collection's array (0 = out, 1 = in), which then gets colormapped to blue
        # (out) and red (in).
        self.collection = RegularPolyCollection(
            6, sizes=(100,), offset_transform=ax.transData,
            offsets=data, array=np.zeros(len(data)),
            clim=(0, 1), cmap=mcolors.ListedColormap(["tab:blue", "tab:red"]))
        ax.add_collection(self.collection)
        canvas = ax.figure.canvas
        canvas.mpl_connect('button_press_event', self.on_press)
        canvas.mpl_connect('button_release_event', self.on_release)

    def callback(self, verts):
        data = self.collection.get_offsets()
        self.collection.set_array(path.Path(verts).contains_points(data))
        canvas = self.collection.figure.canvas
        canvas.draw_idle()
        del self.lasso

    def on_press(self, event):
        canvas = self.collection.figure.canvas
        if event.inaxes is not self.collection.axes or canvas.widgetlock.locked():
            return
        self.lasso = Lasso(event.inaxes, (event.xdata, event.ydata), self.callback)
        canvas.widgetlock(self.lasso)  # acquire a lock on the widget drawing

    def on_release(self, event):
        canvas = self.collection.figure.canvas
        if hasattr(self, 'lasso') and canvas.widgetlock.isowner(self.lasso):
            canvas.widgetlock.release(self.lasso)
```

### Step 3: Create the Plot

Now, use the `LassoManager` class to create an interactive plot. The `np.random.rand` function generates random data points that will be plotted.

```python
if __name__ == '__main__':
    np.random.seed(19680801)
    ax = plt.figure().add_subplot(
        xlim=(0, 1), ylim=(0, 1), title='Lasso points using left mouse button')
    manager = LassoManager(ax, np.random.rand(100, 2))
    plt.show()
```

## Summary

In this lab, you learned how to use Matplotlib to create an interactive plot that allows users to select a set of points using a lasso tool. You also learned how to use a callback function to change the color of the selected points. This functionality can be extended to other projects that require interactive data selection.
