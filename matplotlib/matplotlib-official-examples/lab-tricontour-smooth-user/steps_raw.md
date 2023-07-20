# Python Matplotlib Tricontour Smooth User Lab

## Introduction

This lab will guide you through the process of creating high-resolution tricontours on user-defined triangular grids using Matplotlib. You will learn how to create a Triangulation, refine data, and plot the triangulation and high-resolution iso-contours.

## Steps

### Step 1: Analytical Test Function

In this step, we define an analytical test function that will be used to generate z-values for the triangulation. The function is called `function_z` and takes two arguments, `x` and `y`. It calculates `z` based on the values of `x` and `y`, and returns the normalized `z` values.

```python
def function_z(x, y):
    r1 = np.sqrt((0.5 - x)**2 + (0.5 - y)**2)
    theta1 = np.arctan2(0.5 - x, 0.5 - y)
    r2 = np.sqrt((-x - 0.2)**2 + (-y - 0.2)**2)
    theta2 = np.arctan2(-x - 0.2, -y - 0.2)
    z = -(2 * (np.exp((r1 / 10)**2) - 1) * 30. * np.cos(7. * theta1) +
          (np.exp((r2 / 10)**2) - 1) * 30. * np.cos(11. * theta2) +
          0.7 * (x**2 + y**2))
    return (np.max(z) - z) / (np.max(z) - np.min(z))
```

### Step 2: Creating a Triangulation

In this step, we create the x and y coordinates of the points using `np.linspace` and `np.repeat`. We then use the `function_z` defined in Step 1 to calculate the z-values. Finally, we create the Triangulation using `tri.Triangulation`.

```python
n_angles = 20
n_radii = 10
min_radius = 0.15
radii = np.linspace(min_radius, 0.95, n_radii)

angles = np.linspace(0, 2 * np.pi, n_angles, endpoint=False)
angles = np.repeat(angles[..., np.newaxis], n_radii, axis=1)
angles[:, 1::2] += np.pi / n_angles

x = (radii * np.cos(angles)).flatten()
y = (radii * np.sin(angles)).flatten()
z = function_z(x, y)

triang = tri.Triangulation(x, y)
triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                         y[triang.triangles].mean(axis=1))
                < min_radius)
```

### Step 3: Refine Data

In this step, we use `tri.UniformTriRefiner` to refine the data. We use the `refine_field` method to refine the `z` values and create a new Triangulation with higher resolution.

```python
refiner = tri.UniformTriRefiner(triang)
tri_refi, z_test_refi = refiner.refine_field(z, subdiv=3)
```

### Step 4: Plot Triangulation and High-resolution Iso-contours

In this step, we plot the Triangulation and high-resolution iso-contours using `ax.triplot`, `ax.tricontourf`, and `ax.tricontour`.

```python
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.triplot(triang, lw=0.5, color='white')

levels = np.arange(0., 1., 0.025)
ax.tricontourf(tri_refi, z_test_refi, levels=levels, cmap='terrain')
ax.tricontour(tri_refi, z_test_refi, levels=levels,
              colors=['0.25', '0.5', '0.5', '0.5', '0.5'],
              linewidths=[1.0, 0.5, 0.5, 0.5, 0.5])

ax.set_title("High-resolution tricontouring")

plt.show()
```

## Summary

In this lab, you learned how to create high-resolution tricontours on user-defined triangular grids using Matplotlib. You learned how to create a Triangulation, refine data, and plot the triangulation and high-resolution iso-contours.
