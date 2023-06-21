# Python Matplotlib Tutorial Lab

## Contour Plot of Irregularly Spaced Data

### Introduction

This lab demonstrates how to create a contour plot of irregularly spaced data in Python using Matplotlib. The contour plot shows the 2D distribution of data values using iso-contours or contour lines. In this example, we will compare a contour plot of irregularly spaced data interpolated on a regular grid versus a tricontour plot for an unstructured triangular grid.

### Steps

#### Step 1: Import necessary libraries

We start by importing the necessary libraries for this example: `matplotlib.pyplot` and `numpy`. Additionally, we import `matplotlib.tri` for triangulation of the data.

```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.tri as tri
```

#### Step 2: Generate random data

We generate random data using NumPy's `np.random.uniform` method. We generate `npts = 200` data points with x and y values between -2 and 2. We also calculate the z values using the function `z = x * np.exp(-x**2 - y**2)`.

```python
np.random.seed(19680801)
npts = 200
x = np.random.uniform(-2, 2, npts)
y = np.random.uniform(-2, 2, npts)
z = x * np.exp(-x**2 - y**2)
```

#### Step 3: Interpolation on a grid

We create a contour plot of irregularly spaced data coordinates via interpolation on a grid. We first create grid values for x and y using `np.linspace`. We then linearly interpolate the data (x, y) on a grid defined by (xi, yi) using `tri.LinearTriInterpolator`. We plot the interpolated data with the usual `axes.Axes.contour`.

```python
ngridx = 100
ngridy = 200
xi = np.linspace(-2.1, 2.1, ngridx)
yi = np.linspace(-2.1, 2.1, ngridy)

triang = tri.Triangulation(x, y)
interpolator = tri.LinearTriInterpolator(triang, z)
Xi, Yi = np.meshgrid(xi, yi)
zi = interpolator(Xi, Yi)

fig, ax1 = plt.subplots()
cntr1 = ax1.contourf(xi, yi, zi, levels=14, cmap="RdBu_r")
ax1.plot(x, y, 'ko', ms=3)
ax1.set(xlim=(-2, 2), ylim=(-2, 2))
ax1.set_title('Contour Plot of Irregularly Spaced Data Interpolated on a Grid')
fig.colorbar(cntr1, ax=ax1)
plt.show()
```

#### Step 4: Tricontour

We plot the same data using a tricontour plot by directly supplying the unordered, irregularly spaced coordinates to `axes.Axes.tricontour`.

```python
fig, ax2 = plt.subplots()
cntr2 = ax2.tricontourf(x, y, z, levels=14, cmap="RdBu_r")
ax2.plot(x, y, 'ko', ms=3)
ax2.set(xlim=(-2, 2), ylim=(-2, 2))
ax2.set_title('Tricontour Plot of Irregularly Spaced Data')
fig.colorbar(cntr2, ax=ax2)
plt.show()
```

### Summary

This lab demonstrated how to create a contour plot of irregularly spaced data in Python using Matplotlib. We compared a contour plot of irregularly spaced data interpolated on a regular grid versus a tricontour plot for an unstructured triangular grid. The `axes.Axes.contour` and `axes.Axes.tricontour` methods were used to create the contour plots.
