# Python Matplotlib AnnotationBbox Lab

## Introduction

In this lab, we will learn how to use AnnotationBbox in Matplotlib to annotate figures using text, shapes, and images. AnnotationBbox is a more fine-grained control method than Axes.annotate. We will go through three different OffsetBoxes: TextArea, DrawingArea, and OffsetImage.

## Steps

### Step 1: Plotting Points

To start, let's plot two points that we will annotate later.

```python
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

# Define a 1st position to annotate (display it with a marker)
xy1 = (0.5, 0.7)
ax.plot(xy1[0], xy1[1], ".r")

# Define a 2nd position to annotate (don't display with a marker this time)
xy2 = [0.3, 0.55]

# Fix the display limits to see everything
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

plt.show()
```

### Step 2: Annotating with TextArea

Now let's annotate the first point using a TextArea.

```python
from matplotlib.offsetbox import AnnotationBbox, TextArea

# Annotate the 1st position with a text box ('Test 1')
offsetbox = TextArea("Test 1")

ab = AnnotationBbox(offsetbox, xy1,
                    xybox=(-20, 40),
                    xycoords='data',
                    boxcoords="offset points",
                    arrowprops=dict(arrowstyle="->"),
                    bboxprops=dict(boxstyle="sawtooth"))

ax.add_artist(ab)

plt.show()
```

### Step 3: Annotating with DrawingArea

Next, let's annotate the second point with a circle patch using DrawingArea.

```python
from matplotlib.offsetbox import DrawingArea
from matplotlib.patches import Circle

# Annotate the 2nd position with a circle patch
da = DrawingArea(20, 20, 0, 0)
p = Circle((10, 10), 10)
da.add_artist(p)

ab = AnnotationBbox(da, xy2,
                    xybox=(1., xy2[1]),
                    xycoords='data',
                    boxcoords=("axes fraction", "data"),
                    box_alignment=(0.2, 0.5),
                    arrowprops=dict(arrowstyle="->"),
                    bboxprops=dict(alpha=0.5))

ax.add_artist(ab)

plt.show()
```

### Step 4: Annotating with OffsetImage

Finally, let's annotate the second point with an OffsetImage using an image of Grace Hopper.

```python
from matplotlib.cbook import get_sample_data
from matplotlib.offsetbox import OffsetImage

# Annotate the 2nd position with an image (a generated array of pixels)
arr = np.arange(100).reshape((10, 10))
im = OffsetImage(arr, zoom=2)
im.image.axes = ax

ab = AnnotationBbox(im, xy2,
                    xybox=(-50., 50.),
                    xycoords='data',
                    boxcoords="offset points",
                    pad=0.3,
                    arrowprops=dict(arrowstyle="->"))

ax.add_artist(ab)

# Annotate the 2nd position with another image (a Grace Hopper portrait)
with get_sample_data("grace_hopper.jpg") as file:
    arr_img = plt.imread(file)

imagebox = OffsetImage(arr_img, zoom=0.2)
imagebox.image.axes = ax

ab = AnnotationBbox(imagebox, xy2,
                    xybox=(120., -80.),
                    xycoords='data',
                    boxcoords="offset points",
                    pad=0.5,
                    arrowprops=dict(
                        arrowstyle="->",
                        connectionstyle="angle,angleA=0,angleB=90,rad=3")
                    )

ax.add_artist(ab)

plt.show()
```

## Summary

In this lab, we have learned how to use AnnotationBbox in Matplotlib to annotate figures using text, shapes, and images. We have gone through three different OffsetBoxes: TextArea, DrawingArea, and OffsetImage. By using AnnotationBbox, we have more fine-grained control over annotations than using Axes.annotate.
