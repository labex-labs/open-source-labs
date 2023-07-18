# Primary 3D View Planes Tutorial

## Introduction

In this tutorial, we will learn how to generate an "unfolded" 3D plot using Matplotlib that shows each of the primary 3D view planes. We will also label the elevation, azimuth, and roll angles required for each view. This image can be printed out and folded into a box where each plane forms a side of the box.

## Steps

### Step 1: Import necessary libraries

We start by importing the necessary libraries for this tutorial, which includes Matplotlib.

```python
import matplotlib.pyplot as plt
```

### Step 2: Define a function to annotate axes

We define a function `annotate_axes` that we will use later to label each of the primary 3D view planes with their respective angles.

```python
def annotate_axes(ax, text, fontsize=18):
    ax.text(x=0.5, y=0.5, z=0.5, s=text,
            va="center", ha="center", fontsize=fontsize, color="black")
```

### Step 3: Define the primary 3D view planes and their angles

We define the primary 3D view planes and their corresponding elevation, azimuth, and roll angles.

```python
views = [('XY',   (90, -90, 0)),
         ('XZ',    (0, -90, 0)),
         ('YZ',    (0,   0, 0)),
         ('-XY', (-90,  90, 0)),
         ('-XZ',   (0,  90, 0)),
         ('-YZ',   (0, 180, 0))]
```

### Step 4: Define the layout of the 3D plot

We define the layout of the 3D plot using a list of lists. The `'.'` in the list represents an empty subplot.

```python
layout = [['XY',  '.',   'L',   '.'],
          ['XZ', 'YZ', '-XZ', '-YZ'],
          ['.',   '.', '-XY',   '.']]
```

### Step 5: Create the 3D plot

We use `subplot_mosaic` to create the 3D plot based on the layout defined in step 4.

```python
fig, axd = plt.subplot_mosaic(layout, subplot_kw={'projection': '3d'},
                              figsize=(12, 8.5))
```

### Step 6: Set the properties of each primary 3D view plane

We set the properties of each primary 3D view plane, including the labels for the x, y, and z axes, the projection type, and the view angles.

```python
for plane, angles in views:
    axd[plane].set_xlabel('x')
    axd[plane].set_ylabel('y')
    axd[plane].set_zlabel('z')
    axd[plane].set_proj_type('ortho')
    axd[plane].view_init(elev=angles[0], azim=angles[1], roll=angles[2])
    axd[plane].set_box_aspect(None, zoom=1.25)
```

### Step 7: Label each primary 3D view plane

We use the `annotate_axes` function defined in step 2 to label each primary 3D view plane with its respective angles.

```python
for plane, angles in views:
    label = f'{plane}\n{angles}'
    annotate_axes(axd[plane], label, fontsize=14)
```

### Step 8: Customize the tick labels and axis labels for each primary 3D view plane

We customize the tick labels and axis labels for each primary 3D view plane to remove any unnecessary labels.

```python
for plane in ('XY', '-XY'):
    axd[plane].set_zticklabels([])
    axd[plane].set_zlabel('')
for plane in ('XZ', '-XZ'):
    axd[plane].set_yticklabels([])
    axd[plane].set_ylabel('')
for plane in ('YZ', '-YZ'):
    axd[plane].set_xticklabels([])
    axd[plane].set_xlabel('')
```

### Step 9: Add a label to the center subplot

We add a label to the center subplot to indicate that this is a primary 3D view planes plot.

```python
label = 'mplot3d primary view planes\n' + 'ax.view_init(elev, azim, roll)'
annotate_axes(axd['L'], label, fontsize=18)
axd['L'].set_axis_off()
```

### Step 10: Display the 3D plot

We display the 3D plot using `plt.show()`.

```python
plt.show()
```

## Summary

In this tutorial, we learned how to generate an "unfolded" 3D plot that shows each of the primary 3D view planes using Matplotlib. We also labeled the elevation, azimuth, and roll angles required for each view and customized the tick labels and axis labels for each primary 3D view plane. This image can be printed out and folded into a box where each plane forms a side of the box.
