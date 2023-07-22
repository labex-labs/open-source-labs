# Matplotlib GridHelperCurveLinear Tutorial

## Introduction

This lab provides a step-by-step guide on how to use GridHelperCurveLinear to define custom grids and ticklines by applying a transformation on the grid. We will use Python's Matplotlib library to create custom grids and ticklines.

## Steps

### Step 1: Import Required Libraries

The first step is to import the required libraries, including `matplotlib.pyplot`, `numpy`, `ExtremeFinderSimple`, `MaxNLocator`, and `GridHelperCurveLinear`.

```python
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axisartist.axislines import Axes
from mpl_toolkits.axisartist.grid_finder import (ExtremeFinderSimple, MaxNLocator)
from mpl_toolkits.axisartist.grid_helper_curvelinear import GridHelperCurveLinear
```

### Step 2: Define Transformation Functions

The second step is to define the transformation functions. In this example, we will use the `tr` function to transform the x-axis values and leave the y-axis values unchanged. The `inv_tr` function will be used to invert the transformation.

```python
def tr(x, y):
    return np.sign(x)*abs(x)**.5, y

def inv_tr(x, y):
    return np.sign(x)*x**2, y
```

### Step 3: Define GridHelperCurveLinear

The third step is to define the GridHelperCurveLinear instance. We will use the transformation functions defined in Step 2 to transform the grid. We will also set the `grid_locator1` and `grid_locator2` to `MaxNLocator(nbins=6)` to increase the tick density.

```python
grid_helper = GridHelperCurveLinear(
    (tr, inv_tr),
    extreme_finder=ExtremeFinderSimple(20, 20),
    grid_locator1=MaxNLocator(nbins=6), grid_locator2=MaxNLocator(nbins=6))
```

### Step 4: Define Axes and Display Image

The fourth step is to define the axes using the `grid_helper` instance created in Step 3. We will also display an image using the `imshow` function.

```python
ax1 = fig.add_subplot(axes_class=Axes, grid_helper=grid_helper)
ax1.imshow(np.arange(25).reshape(5, 5), vmax=50, cmap=plt.cm.gray_r, origin="lower")
```

### Step 5: Create the Figure

The final step is to create the figure using the `plt.figure` function. We will set the figure size to (7, 4) and call the `curvelinear_test1` function created in Steps 2-4.

```python
if __name__ == "__main__":
    fig = plt.figure(figsize=(7, 4))
    curvelinear_test1(fig)
    plt.show()
```

## Summary

In this lab, we learned how to use GridHelperCurveLinear to define custom grids and ticklines by applying a transformation on the grid. We used Python's Matplotlib library to create a custom grid and ticklines for a 5x5 matrix displayed on the axes.
