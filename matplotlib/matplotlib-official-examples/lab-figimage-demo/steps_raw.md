# Matplotlib Figure Image Lab

## Introduction

In this lab, you will learn how to use Matplotlib's `figimage` function to place images directly in a figure, without the need for Axes objects. This can be useful when you want to include images that are not part of your plot, such as a logo or watermark.

## Steps

### Step 1: Importing the necessary libraries

First, we need to import the necessary libraries, which are `matplotlib.pyplot` and `numpy`. We will use `numpy` to create an array of random values that we will use as our image.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Creating the figure and image

Next, we create the figure and the image that we want to place in it. In this example, we create a 100x100 array of random values and set the values in the right half of the image to 1. We then create two separate instances of the image, each with a different position and opacity.

```python
fig = plt.figure()
Z = np.arange(10000).reshape((100, 100))
Z[:, 50:] = 1

im1 = fig.figimage(Z, xo=50, yo=0, origin='lower')
im2 = fig.figimage(Z, xo=100, yo=100, alpha=.8, origin='lower')
```

### Step 3: Showing the figure

Finally, we display the figure with the images using the `show()` function.

```python
plt.show()
```

## Summary

In this lab, we learned how to use Matplotlib's `figimage` function to place images directly in a figure. This can be useful when you want to include images that are not part of your plot. By following the steps outlined in this lab, you should now have a better understanding of how to create and display images in Matplotlib figures.
