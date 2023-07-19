# Python Matplotlib Tutorial: Creating a Bezier Curve

## Introduction

In this tutorial, we will learn how to create a Bezier Curve using Python's Matplotlib library. A Bezier Curve is a mathematical curve that is commonly used in computer graphics to create smooth and aesthetically pleasing shapes. We will create a simple example of a Bezier Curve using Matplotlib's `PathPatch` object.

## Steps

### Step 1: Importing Libraries

To create a Bezier Curve using Matplotlib, we need to import the necessary libraries. We will import `matplotlib.pyplot` for creating the plot and `matplotlib.patches` for creating the `PathPatch` object.

```python
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.path as mpath
```

### Step 2: Creating the Path

Next, we will create the `Path` object for the Bezier Curve. The `Path` object takes in a list of vertices and codes that specify the type of path between the vertices. In this case, we will use a `MOVETO` code to move to the starting point, followed by two `CURVE3` codes to specify the control points and ending point, and finally a `CLOSEPOLY` code to close the path.

```python
Path = mpath.Path

bezier_path = Path([(0, 0), (1, 0), (1, 1), (0, 0)],
                   [Path.MOVETO, Path.CURVE3, Path.CURVE3, Path.CLOSEPOLY])
```

### Step 3: Creating the PathPatch Object

Now that we have the `Path` object, we can create the `PathPatch` object that will be used to draw the Bezier Curve on the plot. We will set the `facecolor` to `'none'` so that only the curve is drawn and not filled.

```python
bezier_patch = mpatches.PathPatch(bezier_path, fc="none")
```

### Step 4: Creating the Plot

We can now create the plot by adding the `PathPatch` object to the axes and plotting a red point that should lie on the curve. We will also set the title of the plot to `'Bezier Curve'`.

```python
fig, ax = plt.subplots()

ax.add_patch(bezier_patch)
ax.plot([0.75], [0.25], "ro")
ax.set_title('Bezier Curve')

plt.show()
```

The final code should look like this:

```python
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.path as mpath

Path = mpath.Path

bezier_path = Path([(0, 0), (1, 0), (1, 1), (0, 0)],
                   [Path.MOVETO, Path.CURVE3, Path.CURVE3, Path.CLOSEPOLY])

bezier_patch = mpatches.PathPatch(bezier_path, fc="none")

fig, ax = plt.subplots()

ax.add_patch(bezier_patch)
ax.plot([0.75], [0.25], "ro")
ax.set_title('Bezier Curve')

plt.show()
```

## Summary

In this tutorial, we learned how to create a Bezier Curve using Python's Matplotlib library. We used the `Path` and `PathPatch` objects to create the curve and added it to a plot. We also plotted a red point on the curve to show that it lies on the curve. The Bezier Curve is commonly used in computer graphics to create smooth and aesthetically pleasing shapes.
