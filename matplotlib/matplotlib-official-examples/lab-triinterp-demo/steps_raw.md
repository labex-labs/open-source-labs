# Interpolation from Triangular to Quad Grid

## Introduction

In this lab, you will learn how to use Python's Matplotlib library to interpolate data from a triangular grid to a quad grid. We will start by creating a triangulation and then interpolate the data using linear and cubic methods. Finally, we will plot the results.

## Steps

### Step 1: Create Triangulation

The first step is to create a triangulation using the given x, y, and triangles data. We will then plot the triangulation.

```python
# Create triangulation.
x = np.asarray([0, 1, 2, 3, 0.5, 1.5, 2.5, 1, 2, 1.5])
y = np.asarray([0, 0, 0, 0, 1.0, 1.0, 1.0, 2, 2, 3.0])
triangles = [[0, 1, 4], [1, 2, 5], [2, 3, 6], [1, 5, 4], [2, 6, 5], [4, 5, 7],
             [5, 6, 8], [5, 8, 7], [7, 8, 9]]
triang = mtri.Triangulation(x, y, triangles)

# Plot the triangulation.
plt.triplot(triang, 'ko-')
plt.title('Triangular grid')
plt.show()
```

### Step 2: Interpolate Data using Linear Method

The second step is to interpolate the data using the linear method. We will create a regularly-spaced quad grid and then use the LinearTriInterpolator method to interpolate the data. Finally, we will plot the interpolated data.

```python
# Interpolate to regularly-spaced quad grid.
z = np.cos(1.5 * x) * np.cos(1.5 * y)
xi, yi = np.meshgrid(np.linspace(0, 3, 20), np.linspace(0, 3, 20))

# Interpolate using linear method.
interp_lin = mtri.LinearTriInterpolator(triang, z)
zi_lin = interp_lin(xi, yi)

# Plot the interpolated data.
plt.contourf(xi, yi, zi_lin)
plt.plot(xi, yi, 'k-', lw=0.5, alpha=0.5)
plt.plot(xi.T, yi.T, 'k-', lw=0.5, alpha=0.5)
plt.title("Linear interpolation")
plt.show()
```

### Step 3: Interpolate Data using Cubic Method

The third step is to interpolate the data using the cubic method. We will use the CubicTriInterpolator method with the kind parameter set to 'geom' or 'min_E'. Finally, we will plot the interpolated data.

```python
# Interpolate using cubic method with kind=geom.
interp_cubic_geom = mtri.CubicTriInterpolator(triang, z, kind='geom')
zi_cubic_geom = interp_cubic_geom(xi, yi)

# Plot the interpolated data.
plt.contourf(xi, yi, zi_cubic_geom)
plt.plot(xi, yi, 'k-', lw=0.5, alpha=0.5)
plt.plot(xi.T, yi.T, 'k-', lw=0.5, alpha=0.5)
plt.title("Cubic interpolation, kind='geom'")
plt.show()

# Interpolate using cubic method with kind=min_E.
interp_cubic_min_E = mtri.CubicTriInterpolator(triang, z, kind='min_E')
zi_cubic_min_E = interp_cubic_min_E(xi, yi)

# Plot the interpolated data.
plt.contourf(xi, yi, zi_cubic_min_E)
plt.plot(xi, yi, 'k-', lw=0.5, alpha=0.5)
plt.plot(xi.T, yi.T, 'k-', lw=0.5, alpha=0.5)
plt.title("Cubic interpolation, kind='min_E'")
plt.show()
```

## Summary

In this lab, we learned how to use Python's Matplotlib library to interpolate data from a triangular grid to a quad grid. We started by creating a triangulation and then interpolated the data using linear and cubic methods. Finally, we plotted the results.
