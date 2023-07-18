# Python Matplotlib Tutorial

## Introduction

In this lab, you will learn how to use Matplotlib to create a gradient plot of an electrical dipole. You will learn how to create a triangulation, refine data, and compute the electrical field. Finally, you will plot the triangulation, the potential iso-contours, and the vector field.

## Steps

### Step 1: Create the x and y coordinates of the points

```python
n_angles = 30
n_radii = 10
min_radius = 0.2
radii = np.linspace(min_radius, 0.95, n_radii)

angles = np.linspace(0, 2 * np.pi, n_angles, endpoint=False)
angles = np.repeat(angles[..., np.newaxis], n_radii, axis=1)
angles[:, 1::2] += np.pi / n_angles

x = (radii*np.cos(angles)).flatten()
y = (radii*np.sin(angles)).flatten()
```

Explanation:

- `n_angles` is the number of angles in a circle.
- `n_radii` is the number of circles.
- `min_radius` is the minimum radius of the circles.
- `radii` is an array of radii.
- `angles` is an array of angles.
- `x` is an array of x-coordinates.
- `y` is an array of y-coordinates.

### Step 2: Compute the electrical potential of a dipole

```python
def dipole_potential(x, y):
    """The electric dipole potential V, at position *x*, *y*."""
    r_sq = x**2 + y**2
    theta = np.arctan2(y, x)
    z = np.cos(theta)/r_sq
    return (np.max(z) - z) / (np.max(z) - np.min(z))

V = dipole_potential(x, y)
```

Explanation:

- `dipole_potential` is a function that calculates the electrical dipole potential.
- `V` is an array of electrical dipole potentials.

### Step 3: Create the Triangulation

```python
triang = Triangulation(x, y)

triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                         y[triang.triangles].mean(axis=1))
                < min_radius)
```

Explanation:

- `Triangulation` is a class that creates a Delaunay triangulation from a set of points.
- `triang` is an instance of the `Triangulation` class.
- `triang.set_mask` masks off unwanted triangles.

### Step 4: Refine data

```python
refiner = UniformTriRefiner(triang)
tri_refi, z_test_refi = refiner.refine_field(V, subdiv=3)
```

Explanation:

- `UniformTriRefiner` is a class that refines a triangulation to create a more accurate plot.
- `refiner` is an instance of the `UniformTriRefiner` class.
- `tri_refi` and `z_test_refi` are refined triangulation and potential values, respectively.

### Step 5: Compute the electrical field

```python
tci = CubicTriInterpolator(triang, -V)

(Ex, Ey) = tci.gradient(triang.x, triang.y)
E_norm = np.sqrt(Ex**2 + Ey**2)
```

Explanation:

- `CubicTriInterpolator` is a class that interpolates data using a cubic polynomial.
- `tci` is an instance of the `CubicTriInterpolator` class.
- `(Ex, Ey)` is the electrical field.
- `E_norm` is the normalized electrical field.

### Step 6: Plot the triangulation, the potential iso-contours, and the vector field

```python
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.use_sticky_edges = False
ax.margins(0.07)

ax.triplot(triang, color='0.8')

levels = np.arange(0., 1., 0.01)
ax.tricontour(tri_refi, z_test_refi, levels=levels, cmap='hot',
              linewidths=[2.0, 1.0, 1.0, 1.0])

ax.quiver(triang.x, triang.y, Ex/E_norm, Ey/E_norm,
          units='xy', scale=10., zorder=3, color='blue',
          width=0.007, headwidth=3., headlength=4.)

ax.set_title('Gradient Plot: Electrical Dipole')
plt.show()
```

Explanation:

- `fig` and `ax` are the figure and axes objects, respectively.
- `ax.set_aspect` sets the aspect ratio of the axes.
- `ax.use_sticky_edges` and `ax.margins` set the margins of the axes.
- `ax.triplot` plots the triangulation.
- `ax.tricontour` plots the potential iso-contours.
- `ax.quiver` plots the vector field.
- `ax.set_title` sets the title of the plot.

## Summary

In this lab, you learned how to use Matplotlib to create a gradient plot of an electrical dipole. You learned how to create a triangulation, refine data, and compute the electrical field. Finally, you plotted the triangulation, the potential iso-contours, and the vector field.
