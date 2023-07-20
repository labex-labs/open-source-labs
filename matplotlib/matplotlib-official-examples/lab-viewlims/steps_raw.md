# Matplotlib Zooming Lab

## Introduction

In data visualization, zooming in on a specific area of a plot can be extremely useful to better understand and analyze the data. Matplotlib, a popular data visualization library for Python, provides a way to create two identical panels and zoom in on the right panel to show a rectangle in the first panel, denoting the zoomed region. In this lab, we will learn how to create this interactive zooming feature in Matplotlib.

## Steps

### Step 1: Import necessary libraries

We will first import the necessary libraries, including Matplotlib and NumPy.

```python
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.patches import Rectangle
```

### Step 2: Create the UpdatingRect class

We will create a subclass of Rectangle called UpdatingRect. This class is called with an Axes instance, causing the rectangle to update its shape to match the bounds of the Axes.

```python
class UpdatingRect(Rectangle):
    def __call__(self, ax):
        self.set_bounds(*ax.viewLim.bounds)
        ax.figure.canvas.draw_idle()
```

### Step 3: Create the MandelbrotDisplay class

We will create a class called MandelbrotDisplay that will regenerate a fractal set as we zoom in, so that we can actually see the increasing detail. A box in the left panel will show the area to which we are zoomed.

```python
class MandelbrotDisplay:
    def __init__(self, h=500, w=500, niter=50, radius=2., power=2):
        self.height = h
        self.width = w
        self.niter = niter
        self.radius = radius
        self.power = power

    def compute_image(self, xstart, xend, ystart, yend):
        self.x = np.linspace(xstart, xend, self.width)
        self.y = np.linspace(ystart, yend, self.height).reshape(-1, 1)
        c = self.x + 1.0j * self.y
        threshold_time = np.zeros((self.height, self.width))
        z = np.zeros(threshold_time.shape, dtype=complex)
        mask = np.ones(threshold_time.shape, dtype=bool)
        for i in range(self.niter):
            z[mask] = z[mask]**self.power + c[mask]
            mask = (np.abs(z) < self.radius)
            threshold_time += mask
        return threshold_time

    def ax_update(self, ax):
        ax.set_autoscale_on(False)
        self.width, self.height = \
            np.round(ax.patch.get_window_extent().size).astype(int)
        vl = ax.viewLim
        extent = vl.x0, vl.x1, vl.y0, vl.y1
        im = ax.images[-1]
        im.set_data(self.compute_image(*extent))
        im.set_extent(extent)
        ax.figure.canvas.draw_idle()
```

### Step 4: Create the plot

We will create the plot by first computing the image using the MandelbrotDisplay class, and then creating two identical panels using subplots. We will add the image to both panels using imshow, and add the UpdatingRect object to the left panel.

```python
md = MandelbrotDisplay()
Z = md.compute_image(-2., 0.5, -1.25, 1.25)

fig1, (ax1, ax2) = plt.subplots(1, 2)
ax1.imshow(Z, origin='lower',
           extent=(md.x.min(), md.x.max(), md.y.min(), md.y.max()))
ax2.imshow(Z, origin='lower',
           extent=(md.x.min(), md.x.max(), md.y.min(), md.y.max()))

rect = UpdatingRect(
    [0, 0], 0, 0, facecolor='none', edgecolor='black', linewidth=1.0)
rect.set_bounds(*ax2.viewLim.bounds)
ax1.add_patch(rect)
```

### Step 5: Add zooming functionality

We will add the zooming functionality by connecting the xlim_changed and ylim_changed events to the UpdatingRect and MandelbrotDisplay objects.

```python
ax2.callbacks.connect('xlim_changed', rect)
ax2.callbacks.connect('ylim_changed', rect)

ax2.callbacks.connect('xlim_changed', md.ax_update)
ax2.callbacks.connect('ylim_changed', md.ax_update)
ax2.set_title("Zoom here")
```

### Step 6: Show the plot

We will show the plot using the show() function.

```python
plt.show()
```

## Summary

In this lab, we learned how to create an interactive zooming feature in Matplotlib using two identical panels and the UpdatingRect and MandelbrotDisplay classes. By adding zooming functionality, we can better understand and analyze the data in our plots.
