# Convert Polar Coordinates to Cartesian Coordinates

We will convert the polar coordinates to Cartesian coordinates:

```python
# Convert polar (radii, angles) coords to cartesian (x, y) coords.
# (0, 0) is manually added at this stage, so there will be no duplicate
# points in the (x, y) plane.
x = np.append(0, (radii*np.cos(angles)).flatten())
y = np.append(0, (radii*np.sin(angles)).flatten())
```
