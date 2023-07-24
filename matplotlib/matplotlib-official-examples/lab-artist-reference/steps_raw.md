# Python Matplotlib Tutorial: Drawing Shapes

## Introduction

In this lab, we will learn how to draw various shapes using Matplotlib library in Python. Matplotlib is a plotting library for the Python programming language and its numerical mathematics extension NumPy. It provides an object-oriented API for embedding plots into applications using general-purpose GUI toolkits like Tkinter, wxPython, Qt, or GTK.

## Steps

### Step 1: Import Libraries

Before we start using Matplotlib, we need to import the necessary libraries.

```python
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.path as mpath
```

### Step 2: Define Shapes

We will define the shapes we want to draw using Matplotlib. In this example, we will draw a circle, a rectangle, a wedge, a regular polygon, an ellipse, an arrow, a path patch, and a fancy box patch.

```python
shapes = [
    mpatches.Circle((0, 0), 0.1, ec="none"),
    mpatches.Rectangle((-0.025, -0.05), 0.05, 0.1, ec="none"),
    mpatches.Wedge((0, 0), 0.1, 30, 270, ec="none"),
    mpatches.RegularPolygon((0, 0), 5, radius=0.1),
    mpatches.Ellipse((0, 0), 0.2, 0.1),
    mpatches.Arrow(-0.05, -0.05, 0.1, 0.1, width=0.1),
    mpatches.PathPatch(mpath.Path([(0, 0), (0.5, 0.5), (1, 0)], [1, 2, 2]), ec="none"),
    mpatches.FancyBboxPatch((-0.025, -0.05), 0.05, 0.1, ec="none",
                            boxstyle=mpatches.BoxStyle("Round", pad=0.02)),
]
```

### Step 3: Draw Shapes

We will now draw the shapes using Matplotlib by iterating through the `shapes` list and adding them to the plot.

```python
fig, ax = plt.subplots()
for shape in shapes:
    ax.add_artist(shape)
plt.xlim([-0.5, 1.5])
plt.ylim([-0.5, 1.5])
plt.axis('off')
plt.show()
```

### Step 4: Customize Shapes

We can customize the shapes by setting various properties such as color, edge color, and alpha.

```python
shapes = [
    mpatches.Circle((0, 0), 0.1, color='red', alpha=0.5),
    mpatches.Rectangle((-0.025, -0.05), 0.05, 0.1, ec="none", color='green', alpha=0.5),
    mpatches.Wedge((0, 0), 0.1, 30, 270, ec="none", color='blue', alpha=0.5),
    mpatches.RegularPolygon((0, 0), 5, radius=0.1, color='orange', alpha=0.5),
    mpatches.Ellipse((0, 0), 0.2, 0.1, color='purple', alpha=0.5),
    mpatches.Arrow(-0.05, -0.05, 0.1, 0.1, width=0.1, color='yellow', alpha=0.5),
    mpatches.PathPatch(mpath.Path([(0, 0), (0.5, 0.5), (1, 0)], [1, 2, 2]), ec="none", color='pink', alpha=0.5),
    mpatches.FancyBboxPatch((-0.025, -0.05), 0.05, 0.1, ec="none", color='brown', alpha=0.5,
                            boxstyle=mpatches.BoxStyle("Round", pad=0.02)),
]

fig, ax = plt.subplots()
for shape in shapes:
    ax.add_artist(shape)
plt.xlim([-0.5, 1.5])
plt.ylim([-0.5, 1.5])
plt.axis('off')
plt.show()
```

### Step 5: Save Plot

We can save the plot as an image file using the `savefig` function.

```python
fig, ax = plt.subplots()
for shape in shapes:
    ax.add_artist(shape)
plt.xlim([-0.5, 1.5])
plt.ylim([-0.5, 1.5])
plt.axis('off')
plt.savefig('shapes.png')
```

## Summary

In this lab, we learned how to draw various shapes using Matplotlib library in Python. We learned how to define shapes, draw shapes, customize shapes, and save the plot as an image file. Matplotlib provides an easy-to-use API for drawing various types of plots and is widely used in data visualization.
