# Python Matplotlib Tutorial

## High-Resolution Tricontouring with Matplotlib

### Introduction

This tutorial demonstrates how to generate high-resolution tricontouring plots with Matplotlib. Tricontouring is a technique used to represent data on an unstructured triangular mesh. It is often used when data is collected at irregularly spaced points, or when the data is inherently triangular in nature. The tutorial will show how to generate a random set of points, perform a Delaunay triangulation on those points, mask out some of the triangles in the mesh, refine and interpolate the data, and finally plot the refined data using Matplotlib's `tricontour` function.

### Steps

#### Import Required Libraries

The first step is to import the required libraries. This tutorial will use NumPy and Matplotlib.

```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.tri import TriAnalyzer, Triangulation, UniformTriRefiner
```

#### Define Test Function

Next, we define a function that represents the results of an experiment. This function will be used to generate the test data points.

```python
def experiment_res(x, y):
    """An analytic function representing experiment results."""
    x = 2 * x
    r1 = np.sqrt((0.5 - x)**2 + (0.5 - y)**2)
    theta1 = np.arctan2(0.5 - x, 0.5 - y)
    r2 = np.sqrt((-x - 0.2)**2 + (-y - 0.2)**2)
    theta2 = np.arctan2(-x - 0.2, -y - 0.2)
    z = (4 * (np.exp((r1/10)**2) - 1) * 30 * np.cos(3 * theta1) +
         (np.exp((r2/10)**2) - 1) * 30 * np.cos(5 * theta2) +
         2 * (x**2 + y**2))
    return (np.max(z) - z) / (np.max(z) - np.min(z))
```

#### Generate Test Data Points

We generate a set of random test data points, with x and y values between -1 and 1. We also generate a corresponding set of z values using the `experiment_res` function defined in step 2.

```python
# User parameters for data test points

# Number of test data points, tested from 3 to 5000 for subdiv=3
n_test = 200

# Random points
random_gen = np.random.RandomState(seed=19680801)
x_test = random_gen.uniform(-1., 1., size=n_test)
y_test = random_gen.uniform(-1., 1., size=n_test)
z_test = experiment_res(x_test, y_test)
```

#### Perform Delaunay Triangulation

We perform a Delaunay triangulation on the test data points using the `Triangulation` function from the `matplotlib.tri` module.

```python
# meshing with Delaunay triangulation
tri = Triangulation(x_test, y_test)
ntri = tri.triangles.shape[0]
```

#### Mask Some Triangles

We mask out some of the triangles in the mesh to simulate invalidated data. We randomly select a subset of triangles based on the `init_mask_frac` parameter.

```python
# Some invalid data are masked out
mask_init = np.zeros(ntri, dtype=bool)
masked_tri = random_gen.randint(0, ntri, int(ntri * init_mask_frac))
mask_init[masked_tri] = True
tri.set_mask(mask_init)
```

#### Improve Triangulation

We use a `TriAnalyzer` to improve the triangulation by removing badly shaped (flat) triangles from the border of the triangulation. We then apply the mask to the triangulation using `set_mask`.

```python
# masking badly shaped triangles at the border of the triangular mesh.
mask = TriAnalyzer(tri).get_flat_tri_mask(min_circle_ratio)
tri.set_mask(mask)
```

#### Refine and Interpolate Data

We refine and interpolate the data using a `UniformTriRefiner`.

```python
# refining the data
refiner = UniformTriRefiner(tri)
tri_refi, z_test_refi = refiner.refine_field(z_test, subdiv=subdiv)
```

#### Plot the Data

We plot the refined data using Matplotlib's `tricontour` function.

```python
# Graphical options for tricontouring
levels = np.arange(0., 1., 0.025)

fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_title("Filtering a Delaunay mesh\n"
             "(application to high-resolution tricontouring)")

# plot of the refined (computed) data contours:
ax.tricontour(tri_refi, z_test_refi, levels=levels, cmap='Blues',
              linewidths=[2.0, 0.5, 1.0, 0.5])

plt.show()
```

### Summary

This tutorial demonstrated how to generate high-resolution tricontouring plots with Matplotlib. We started by generating a set of random test data points, performing a Delaunay triangulation on those points, masking out some of the triangles in the mesh, refining and interpolating the data, and finally plotting the refined data using Matplotlib's `tricontour` function.
