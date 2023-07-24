# Python Matplotlib Tutorial

## Introduction

This lab is a step-by-step tutorial on how to create contour plots using Python Matplotlib. Contour plots are useful for visualizing three-dimensional data in two dimensions. In this tutorial, we will be illustrating simple contour plotting, contours on an image with a colorbar for the contours, and labeled contours.

## Steps

### Step 1: Import Required Libraries

Before we can begin creating our contour plot, we need to import the necessary libraries. We will be using numpy and matplotlib for this tutorial.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Create Data

We need to create the data we will be using to create the contour plot. In this example, we will be creating two 2D Gaussian functions.

```python
delta = 0.025
x = np.arange(-3.0, 3.0, delta)
y = np.arange(-2.0, 2.0, delta)
X, Y = np.meshgrid(x, y)
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
Z = (Z1 - Z2) * 2
```

### Step 3: Create a Simple Contour Plot with Labels

Now that we have our data, we can create a simple contour plot with labels using default colors.

```python
fig, ax = plt.subplots()
CS = ax.contour(X, Y, Z)
ax.clabel(CS, inline=True, fontsize=10)
ax.set_title('Simplest default with labels')
```

### Step 4: Place Contour Labels Manually

We can also place contour labels manually by providing a list of positions (in data coordinate).

```python
fig, ax = plt.subplots()
CS = ax.contour(X, Y, Z)
manual_locations = [
    (-1, -1.4), (-0.62, -0.7), (-2, 0.5), (1.7, 1.2), (2.0, 1.4), (2.4, 1.7)]
ax.clabel(CS, inline=True, fontsize=10, manual=manual_locations)
ax.set_title('labels at selected locations')
```

### Step 5: Set Contour Colors

We can force all the contours to be the same color or set negative contours to be solid instead of dashed.

```python
fig, ax = plt.subplots()
CS = ax.contour(X, Y, Z, 6, colors='k')  # Negative contours default to dashed.
ax.clabel(CS, fontsize=9, inline=True)
ax.set_title('Single color - negative contours dashed')
```

```python
plt.rcParams['contour.negative_linestyle'] = 'solid'
fig, ax = plt.subplots()
CS = ax.contour(X, Y, Z, 6, colors='k')  # Negative contours default to dashed.
ax.clabel(CS, fontsize=9, inline=True)
ax.set_title('Single color - negative contours solid')
```

### Step 6: Manually Specify Contour Colors

We can also manually specify the colors of the contour.

```python
fig, ax = plt.subplots()
CS = ax.contour(X, Y, Z, 6,
                linewidths=np.arange(.5, 4, .5),
                colors=('r', 'green', 'blue', (1, 1, 0), '#afeeee', '0.5'),
                )
ax.clabel(CS, fontsize=9, inline=True)
ax.set_title('Crazy lines')
```

### Step 7: Use a Colormap to Specify Contour Colors

We can use a colormap to specify the colors for the contour lines.

```python
fig, ax = plt.subplots()
im = ax.imshow(Z, interpolation='bilinear', origin='lower',
               cmap=cm.gray, extent=(-3, 3, -2, 2))
levels = np.arange(-1.2, 1.6, 0.2)
CS = ax.contour(Z, levels, origin='lower', cmap='flag', extend='both',
                linewidths=2, extent=(-3, 3, -2, 2))

# Thicken the zero contour.
CS.collections[6].set_linewidth(4)

ax.clabel(CS, levels[1::2],  # label every second level
          inline=True, fmt='%1.1f', fontsize=14)

# make a colorbar for the contour lines
CB = fig.colorbar(CS, shrink=0.8)

ax.set_title('Lines with colorbar')

# We can still add a colorbar for the image, too.
CBI = fig.colorbar(im, orientation='horizontal', shrink=0.8)

# This makes the original colorbar look a bit out of place,
# so let's improve its position.

l, b, w, h = ax.get_position().bounds
ll, bb, ww, hh = CB.ax.get_position().bounds
CB.ax.set_position([ll, b + 0.1*h, ww, h*0.8])
```

### Summary

In this lab, we have learned how to create contour plots using Python Matplotlib. We have covered creating a simple contour plot with labels, placing contour labels manually, setting contour colors, manually specifying contour colors, and using a colormap to specify contour colors.
