# Creating a Delaunay Triangulation

We will create a Delaunay triangulation of the points. First, we will create the x and y coordinates of the points using NumPy.

```python
n_angles = 36
n_radii = 8
min_radius = 0.25
radii = np.linspace(min_radius, 0.95, n_radii)
angles = np.linspace(0, 2 * np.pi, n_angles, endpoint=False)
angles = np.repeat(angles[..., np.newaxis], n_radii, axis=1)
angles[:, 1::2] += np.pi / n_angles
x = (radii * np.cos(angles)).flatten()
y = (radii * np.sin(angles)).flatten()
```

Then, we will create the z coordinates of the points.

```python
z = (np.cos(radii) * np.cos(3 * angles)).flatten()
```

Next, we will create the Triangulation object using the `Triangulation()` function from `matplotlib.tri`. Since we are not specifying the triangles, the Delaunay triangulation will be created automatically.

```python
triang = tri.Triangulation(x, y)
```

Finally, we will mask off unwanted triangles using the `set_mask()` function. In this example, we are setting the mask to exclude triangles with a mean radius less than `min_radius`.

```python
triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                         y[triang.triangles].mean(axis=1))
                < min_radius)
```
