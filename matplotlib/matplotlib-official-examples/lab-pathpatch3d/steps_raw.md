# Drawing Flat Objects in 3D Plot

## Introduction

Matplotlib is a popular data visualization library in Python. It provides a wide range of functions to create different types of plots and charts. One of the features of Matplotlib is the ability to draw flat objects in 3D plots. This lab will guide you through the process of drawing flat objects in 3D plots using Matplotlib.

## Steps

### Step 1: Import Required Libraries

We will start by importing the required libraries, which are Matplotlib, NumPy, and mpl_toolkits.mplot3d.art3d.

```python
import matplotlib.pyplot as plt
import numpy as np
import mpl_toolkits.mplot3d.art3d as art3d
```

### Step 2: Create a 3D Plot

We will create a 3D plot using the `add_subplot` function of Matplotlib. The `projection` parameter is set to '3d' to create a 3D plot.

```python
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
```

### Step 3: Draw a Circle on the Wall

We will draw a circle on the x=0 'wall' of the 3D plot using the `Circle` and `pathpatch_2d_to_3d` functions of Matplotlib.

```python
p = Circle((5, 5), 3)
ax.add_patch(p)
art3d.pathpatch_2d_to_3d(p, z=0, zdir="x")
```

### Step 4: Label the Axes

We will manually label the axes using the `text3d` function. The function takes the position of the text, the text to display, the axis to be treated as the third dimension, and other parameters.

```python
def text3d(ax, xyz, s, zdir="z", size=None, angle=0, usetex=False, **kwargs):
    """
    Plots the string *s* on the axes *ax*, with position *xyz*, size *size*,
    and rotation angle *angle*. *zdir* gives the axis which is to be treated as
    the third dimension. *usetex* is a boolean indicating whether the string
    should be run through a LaTeX subprocess or not.  Any additional keyword
    arguments are forwarded to `.transform_path`.

    Note: zdir affects the interpretation of xyz.
    """
    x, y, z = xyz
    if zdir == "y":
        xy1, z1 = (x, z), y
    elif zdir == "x":
        xy1, z1 = (y, z), x
    else:
        xy1, z1 = (x, y), z

    text_path = TextPath((0, 0), s, size=size, usetex=usetex)
    trans = Affine2D().rotate(angle).translate(xy1[0], xy1[1])

    p1 = PathPatch(trans.transform_path(text_path), **kwargs)
    ax.add_patch(p1)
    art3d.pathpatch_2d_to_3d(p1, z=z1, zdir=zdir)


text3d(ax, (4, -2, 0), "X-axis", zdir="z", size=.5, usetex=False,
       ec="none", fc="k")
text3d(ax, (12, 4, 0), "Y-axis", zdir="z", size=.5, usetex=False,
       angle=np.pi / 2, ec="none", fc="k")
text3d(ax, (12, 10, 4), "Z-axis", zdir="y", size=.5, usetex=False,
       angle=np.pi / 2, ec="none", fc="k")
```

### Step 5: Write a Latex Formula on the Floor

We will write a Latex formula on the z=0 'floor' of the 3D plot using the `text3d` function.

```python
text3d(ax, (1, 5, 0),
       r"$\displaystyle G_{\mu\nu} + \Lambda g_{\mu\nu} = "
       r"\frac{8\pi G}{c^4} T_{\mu\nu}  $",
       zdir="z", size=1, usetex=True,
       ec="none", fc="k")
```

### Step 6: Set Limits and Show Plot

We will set the limits of the x, y, and z axes using the `set_xlim`, `set_ylim`, and `set_zlim` functions of Matplotlib. Finally, we will show the 3D plot using the `show` function of Matplotlib.

```python
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_zlim(0, 10)

plt.show()
```

## Summary

In this lab, we learned how to draw flat objects in 3D plots using Matplotlib. We created a 3D plot, drew a circle on the wall, labeled the axes, wrote a Latex formula on the floor, and set the limits of the axes.
