# Building Histograms with Matplotlib

## Introduction

In this lab, we will learn how to use Matplotlib to build histograms using rectangles and PolyCollections. We will use numpy to generate random data, and then use Matplotlib to visualize the data as a histogram. This lab assumes that you have a basic understanding of Python and Matplotlib.

## Steps

### Step 1: Import the necessary libraries

Before we start, we need to import the necessary libraries. We will be using Matplotlib and numpy in this lab. Open a new Python file and add the following code:

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Set the random seed and generate data

We will use numpy to generate random data. In order to make our results reproducible, we will set a random seed. Add the following code to your file:

```python
np.random.seed(19680801)
data = np.random.randn(1000)
```

### Step 3: Generate the histogram data

Now that we have our random data, we can generate a histogram using numpy. We will use 50 bins to create our histogram. Add the following code:

```python
n, bins = np.histogram(data, 50)
```

### Step 4: Generate the corners of the rectangles

In order to draw our histogram using rectangles, we need to calculate the corners of each rectangle. Add the following code:

```python
left = bins[:-1]
right = bins[1:]
bottom = np.zeros(len(left))
top = bottom + n
```

### Step 5: Generate the Path object and make a patch out of it

Next, we will generate a Path object and make a patch out of it. We will use the Path object to draw our histogram using rectangles. Add the following code:

```python
XY = np.array([[left, left, right, right], [bottom, top, top, bottom]]).T
barpath = path.Path.make_compound_path_from_polys(XY)
patch = patches.PathPatch(barpath)
patch.sticky_edges.y[:] = [0]
axs[0].add_patch(patch)
axs[0].autoscale_view()
```

### Step 6: Draw the histogram using a PathCollection

Instead of using lots of Rectangle instances, we can use a faster method of drawing our histogram using a PathCollection. We will create a compound path directly using vertices and codes. Add the following code:

```python
nrects = len(left)
nverts = nrects*(1+3+1)
verts = np.zeros((nverts, 2))
codes = np.ones(nverts, int) * path.Path.LINETO
codes[0::5] = path.Path.MOVETO
codes[4::5] = path.Path.CLOSEPOLY
verts[0::5, 0] = left
verts[0::5, 1] = bottom
verts[1::5, 0] = left
verts[1::5, 1] = top
verts[2::5, 0] = right
verts[2::5, 1] = top
verts[3::5, 0] = right
verts[3::5, 1] = bottom

barpath = path.Path(verts, codes)
patch = patches.PathPatch(barpath)
patch.sticky_edges.y[:] = [0]
axs[1].add_patch(patch)
axs[1].autoscale_view()
```

### Step 7: Display the histogram

Finally, we can display our histogram using Matplotlib. Add the following code to your file:

```python
plt.show()
```

## Summary

In this lab, we learned how to use Matplotlib to build histograms using rectangles and PolyCollections. We used numpy to generate random data, and then used Matplotlib to visualize the data as a histogram. We also learned how to draw histograms using a PathCollection, which is a faster method than using lots of Rectangle instances.
