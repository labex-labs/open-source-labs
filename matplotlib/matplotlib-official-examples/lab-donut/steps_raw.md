# Matplotlib Tutorial: Creating Donuts Using `~.path.Path` and `~.patches.PathPatch`

## Introduction

In this tutorial, we will create a donut using Matplotlib's `~.path.Path` and `~.patches.PathPatch`. We will use the `make_circle()` function to create the circle and concatenate the inside and outside subpaths together to create the donut.

## Steps

### Step 1: Importing Necessary Libraries

We will start by importing the necessary libraries for this tutorial.

```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
import matplotlib.path as mpath
```

### Step 2: Defining Helper Function

We will define a helper function `wise()` to determine the orientation of the path.

```python
def wise(v):
    if v == 1:
        return "CCW"
    else:
        return "CW"
```

### Step 3: Creating the Circle

We will create the circle using the `make_circle()` function. The function takes the radius of the circle as input and returns the x and y coordinates of the circle.

```python
def make_circle(r):
    t = np.arange(0, np.pi * 2.0, 0.01)
    t = t.reshape((len(t), 1))
    x = r * np.cos(t)
    y = r * np.sin(t)
    return np.hstack((x, y))
```

### Step 4: Creating the Donut

We will create the donut by concatenating the inside and outside subpaths together. We will use `codes` to specify the type of each vertex (MOVETO, LINETO, etc). We will then create a `Path` object using `mpath.Path` and a `PathPatch` object using `mpatches.PathPatch`. We will finally add the `PathPatch` object to the `Axes` object using `ax.add_patch()`.

```python
Path = mpath.Path
fig, ax = plt.subplots()

inside_vertices = make_circle(0.5)
outside_vertices = make_circle(1.0)
codes = np.ones(
    len(inside_vertices), dtype=mpath.Path.code_type) * mpath.Path.LINETO
codes[0] = mpath.Path.MOVETO

for i, (inside, outside) in enumerate(((1, 1), (1, -1), (-1, 1), (-1, -1))):
    # Concatenate the inside and outside subpaths together, changing their
    # order as needed
    vertices = np.concatenate((outside_vertices[::outside],
                               inside_vertices[::inside]))
    # Shift the path
    vertices[:, 0] += i * 2.5
    # The codes will be all "LINETO" commands, except for "MOVETO"s at the
    # beginning of each subpath
    all_codes = np.concatenate((codes, codes))
    # Create the Path object
    path = mpath.Path(vertices, all_codes)
    # Add plot it
    patch = mpatches.PathPatch(path, facecolor='#885500', edgecolor='black')
    ax.add_patch(patch)

    ax.annotate(f"Outside {wise(outside)},\nInside {wise(inside)}",
                (i * 2.5, -1.5), va="top", ha="center")

ax.set_xlim(-2, 10)
ax.set_ylim(-3, 2)
ax.set_title('Mmm, donuts!')
ax.set_aspect(1.0)
plt.show()
```

### Step 5: Summary

In this tutorial, we learned how to create a donut using Matplotlib's `~.path.Path` and `~.patches.PathPatch`. We used the `make_circle()` function to create the circle and concatenated the inside and outside subpaths together to create the donut. We also learned how to specify the type of each vertex and create a `Path` object using `mpath.Path`. Finally, we learned how to create a `PathPatch` object using `mpatches.PathPatch` and add it to the `Axes` object using `ax.add_patch()`.
