# Create the x and y coordinates of the points

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
