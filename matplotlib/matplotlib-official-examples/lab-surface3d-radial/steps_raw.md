# Python Matplotlib Tutorial

## Introduction

This lab is a step-by-step guide to creating a 3D surface with polar coordinates using Python Matplotlib library. This lab assumes basic knowledge of Python programming and the Matplotlib library.

## Steps

### Step 1: Import Required Libraries

We will begin by importing the required libraries for this lab, which include Matplotlib and NumPy. Matplotlib is a plotting library for Python, while NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Create the Mesh

Next, we will create the mesh in polar coordinates and compute corresponding Z. We will create an array of radius values `r`, an array of angle values `p`, and then use NumPy's `meshgrid()` function to create a grid of `R` and `P` values. Finally, we will use the `Z` equation to compute the height of each point on the surface.

```python
r = np.linspace(0, 1.25, 50)
p = np.linspace(0, 2*np.pi, 50)
R, P = np.meshgrid(r, p)
Z = ((R**2 - 1)**2)
```

### Step 3: Express the Mesh in Cartesian System

Now, we will express the mesh in the cartesian system using NumPy's `cos()` and `sin()` functions.

```python
X, Y = R*np.cos(P), R*np.sin(P)
```

### Step 4: Plot the Surface

In this step, we will plot the surface using Matplotlib's `plot_surface()` function. We will use the colormap `YlGnBu_r` to set the color of the surface.

```python
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(X, Y, Z, cmap=plt.cm.YlGnBu_r)
```

### Step 5: Tweak the Limits and Add Labels

Finally, we will tweak the limits of the plot and add axis labels using Matplotlib's `set_zlim()` and `set_xlabel()`, `set_ylabel()`, `set_zlabel()` functions. We will also use LaTeX math mode to write the axis labels.

```python
ax.set_zlim(0, 1)
ax.set_xlabel(r'$\phi_\mathrm{real}$')
ax.set_ylabel(r'$\phi_\mathrm{im}$')
ax.set_zlabel(r'$V(\phi)$')
```

### Summary

In this lab, we have learned how to create a 3D surface with polar coordinates using Python Matplotlib library. We started by importing the required libraries, created a mesh in polar coordinates, expressed the mesh in the cartesian system, plotted the surface, and finally tweaked the limits and added axis labels.
