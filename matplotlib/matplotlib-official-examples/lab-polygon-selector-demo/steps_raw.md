# Select Indices Using Polygon Selector

## Introduction

This lab demonstrates how to use the Polygon Selector tool in Matplotlib to select indices from a collection. The Polygon Selector tool allows the user to select points on a graph by drawing a polygon around them. The selected points are then highlighted while the unselected points are faded out. The indices of the selected points are saved in an array, which can then be used for further analysis.

## Steps

### Step 1: Import Libraries

In this step, we will import the necessary libraries for this lab. We will be using `numpy` and `matplotlib` for data manipulation and visualization.

```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.widgets import PolygonSelector
```

### Step 2: Create Data

In this step, we will create some data to visualize. We will create a scatter plot of points on a grid.

```python
fig, ax = plt.subplots()
grid_size = 5
grid_x = np.tile(np.arange(grid_size), grid_size)
grid_y = np.repeat(np.arange(grid_size), grid_size)
pts = ax.scatter(grid_x, grid_y)
```

### Step 3: Define Selector Class

In this step, we will define a class that will allow us to select points from the scatter plot using the Polygon Selector tool. This class will save the indices of the selected points in an array.

```python
class SelectFromCollection:
    """
    Select indices from a matplotlib collection using `PolygonSelector`.

    Selected indices are saved in the `ind` attribute. This tool fades out the
    points that are not part of the selection (i.e., reduces their alpha
    values). If your collection has alpha < 1, this tool will permanently
    alter the alpha values.

    Note that this tool selects collection objects based on their *origins*
    (i.e., `offsets`).

    Parameters
    ----------
    ax : `~matplotlib.axes.Axes`
        Axes to interact with.
    collection : `matplotlib.collections.Collection` subclass
        Collection you want to select from.
    alpha_other : 0 <= float <= 1
        To highlight a selection, this tool sets all selected points to an
        alpha value of 1 and non-selected points to *alpha_other*.
    """

    def __init__(self, ax, collection, alpha_other=0.3):
        self.canvas = ax.figure.canvas
        self.collection = collection
        self.alpha_other = alpha_other

        self.xys = collection.get_offsets()
        self.Npts = len(self.xys)

        # Ensure that we have separate colors for each object
        self.fc = collection.get_facecolors()
        if len(self.fc) == 0:
            raise ValueError('Collection must have a facecolor')
        elif len(self.fc) == 1:
            self.fc = np.tile(self.fc, (self.Npts, 1))

        self.poly = PolygonSelector(ax, self.onselect, draw_bounding_box=True)
        self.ind = []

    def onselect(self, verts):
        path = Path(verts)
        self.ind = np.nonzero(path.contains_points(self.xys))[0]
        self.fc[:, -1] = self.alpha_other
        self.fc[self.ind, -1] = 1
        self.collection.set_facecolors(self.fc)
        self.canvas.draw_idle()

    def disconnect(self):
        self.poly.disconnect_events()
        self.fc[:, -1] = 1
        self.collection.set_facecolors(self.fc)
        self.canvas.draw_idle()
```

### Step 4: Create Selector Object

In this step, we will create an instance of the Selector class that we defined in Step 3. This will allow us to select points from the scatter plot using the Polygon Selector tool.

```python
selector = SelectFromCollection(ax, pts)
```

### Step 5: Select Points

In this step, we will select points from the scatter plot using the Polygon Selector tool. We can select points by drawing a polygon around them. The selected points will be highlighted while the unselected points will be faded out.

```python
print("Select points in the figure by enclosing them within a polygon.")
print("Press the 'esc' key to start a new polygon.")
print("Try holding the 'shift' key to move all of the vertices.")
print("Try holding the 'ctrl' key to move a single vertex.")
plt.show()
```

### Step 6: Disconnect Selector Object

In this step, we will disconnect the Selector object to release the resources used by the Polygon Selector tool.

```python
selector.disconnect()
```

### Step 7: Print Selected Points

In this step, we will print the coordinates of the selected points.

```python
print('\nSelected points:')
print(selector.xys[selector.ind])
```

## Summary

This lab demonstrates how to use the Polygon Selector tool in Matplotlib to select indices from a scatter plot. The Selector class allows the user to select points by drawing a polygon around them. The selected points are highlighted while the unselected points are faded out. The indices of the selected points are saved in an array, which can be used for further analysis.
